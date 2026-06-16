from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from PyPDF2 import PdfReader
from flashtext import KeywordProcessor
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import pymysql
import requests
import json
import os

app = Flask(__name__)
CORS(app)

# ==========================
# MYSQL CONNECTION
# ==========================

db = pymysql.connect(
    host="localhost",
    user="root",
    password="SRIDKAVI@2005",
    database="resume_analyzer"
)

# ==========================
# SKILLS DATABASE
# ==========================

skill_keywords = [
    "python",
    "java",
    "sql",
    "mysql",
    "flask",
    "machine learning",
    "deep learning",
    "nlp",
    "tensorflow",
    "keras",
    "pandas",
    "numpy",
    "power bi",
    "excel",
    "tableau",
    "data analysis",
    "aws",
    "docker",
    "git",
    "github"
]

keyword_processor = KeywordProcessor(case_sensitive=False)

for skill in skill_keywords:
    keyword_processor.add_keyword(skill)

# ==========================
# PDF TEXT EXTRACTION
# ==========================

def extract_text(pdf_file):

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + " "

    return text

# ==========================
# SKILL EXTRACTION
# ==========================

def extract_skills(text):

    skills = keyword_processor.extract_keywords(
        text.lower()
    )

    return list(set(skills))

# ==========================
# ATS SCORE
# ==========================

def calculate_ats(skills):

    total_required = len(skill_keywords)

    score = int(
        (len(skills) / total_required) * 100
    )

    if score > 100:
        score = 100

    return score

# ==========================
# RESUME SUGGESTIONS
# ==========================

def get_suggestions(text, skills):

    suggestions = []

    if len(skills) < 5:
        suggestions.append(
            "Add more technical skills."
        )

    if "project" not in text.lower():
        suggestions.append(
            "Add project section."
        )

    if "certification" not in text.lower():
        suggestions.append(
            "Add certifications."
        )

    if "internship" not in text.lower():
        suggestions.append(
            "Mention internship experience."
        )

    if "github" not in text.lower():
        suggestions.append(
            "Add GitHub profile."
        )

    return suggestions

# ==========================
# JD MATCHING
# ==========================

def calculate_jd_match(
    resume_text,
    jd_text
):

    documents = [
        resume_text,
        jd_text
    ]

    vectorizer = TfidfVectorizer()

    matrix = vectorizer.fit_transform(
        documents
    )

    similarity = cosine_similarity(
        matrix[0:1],
        matrix[1:2]
    )

    score = round(
        similarity[0][0] * 100,
        2
    )

    return score

# ==========================
# HOME PAGE
# ==========================

@app.route('/')
def index():
    return render_template('index.html')
# ==========================
# RESUME UPLOAD API
# ==========================

@app.route('/upload', methods=['POST'])
def upload_resume():

    if 'resume' not in request.files:
        return jsonify({
            "error": "Resume file not uploaded"
        }), 400

    file = request.files['resume']

    if file.filename == '':
        return jsonify({
            "error": "No file selected"
        }), 400

    try:

        resume_text = extract_text(file)

        skills = extract_skills(
            resume_text
        )

        ats_score = calculate_ats(
            skills
        )

        suggestions = get_suggestions(
            resume_text,
            skills
        )

        cursor = db.cursor()

        cursor.execute(
            """
            INSERT INTO resumes
            (filename, skills, ats_score)
            VALUES (%s,%s,%s)
            """,
            (
                file.filename,
                json.dumps(skills),
                ats_score
            )
        )

        db.commit()

        jobs = []

        try:

            response = requests.get(
                "https://remotive.com/api/remote-jobs"
            )

            if response.status_code == 200:

                data = response.json()

                for job in data["jobs"][:15]:

                    jobs.append({
                        "title": job["title"],
                        "company": job["company_name"],
                        "url": job["url"]
                    })

        except Exception:
            pass

        return jsonify({

            "filename": file.filename,

            "skills": skills,

            "ats_score": ats_score,

            "suggestions": suggestions,

            "jobs": jobs

        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ==========================
# RESUME VS JD MATCHING
# ==========================

@app.route(
    '/jd_match',
    methods=['POST']
)
def jd_match():

    if 'resume' not in request.files:
        return jsonify({
            "error": "Resume missing"
        })

    if 'jd' not in request.files:
        return jsonify({
            "error": "JD missing"
        })

    resume_file = request.files['resume']
    jd_file = request.files['jd']

    try:

        resume_text = extract_text(
            resume_file
        )

        jd_text = extract_text(
            jd_file
        )

        score = calculate_jd_match(
            resume_text,
            jd_text
        )

        resume_skills = extract_skills(
            resume_text
        )

        jd_skills = extract_skills(
            jd_text
        )

        matched = list(
            set(resume_skills)
            &
            set(jd_skills)
        )

        missing = list(
            set(jd_skills)
            -
            set(resume_skills)
        )

        return jsonify({

            "match_score": score,

            "matched_skills": matched,

            "missing_skills": missing

        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        })


# ==========================
# HISTORY PAGE API
# ==========================

@app.route('/history')
def history():

    cursor = db.cursor()

    cursor.execute(
        """
        SELECT *
        FROM resumes
        ORDER BY created_at DESC
        """
    )

    data = cursor.fetchall()

    history_data = []

    for row in data:

        history_data.append({

            "id": row[0],

            "filename": row[1],

            "skills": row[2],

            "ats_score": row[3],

            "created_at": str(row[4])

        })

    return jsonify(
        history_data
    )


# ==========================
# DASHBOARD STATS
# ==========================

@app.route('/dashboard_stats')
def dashboard_stats():

    cursor = db.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM resumes
        """
    )

    total_resumes = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT AVG(ats_score)
        FROM resumes
        """
    )

    avg_score = cursor.fetchone()[0]

    if avg_score is None:
        avg_score = 0

    return jsonify({

        "total_resumes":
        total_resumes,

        "average_ats":
        round(avg_score, 2)
        
    })


# ==========================
# MAIN
# ==========================
@app.route('/history_page')
def history_page():
    return render_template(
        'history.html'
    )

@app.route('/jd_page')
def jd_page():
    return render_template(
        'jd_match.html'
    )

if __name__ == "__main__":

    app.run(
        debug=True,
        port=8080
    )
