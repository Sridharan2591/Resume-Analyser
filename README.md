# Resume-Analyser
# 🚀 AI Resume Analyzer & Career Guidance System

An intelligent web-based application that analyzes resumes, calculates ATS scores, matches resumes with job descriptions, recommends jobs, and provides personalized learning resources to help users improve their employability.

---

## 📌 Project Overview

The AI Resume Analyzer is designed to help students, fresh graduates, and job seekers evaluate their resumes against industry standards. The system extracts skills from uploaded resumes, calculates an ATS (Applicant Tracking System) score, suggests improvements, matches resumes with job descriptions, and recommends relevant job opportunities and coding practice resources.

---

## ✨ Features

### 📄 Resume Upload & Analysis

* Upload PDF resumes
* Extract resume text automatically
* Identify technical skills and keywords

### 🎯 ATS Score Calculation

* Analyze resume content
* Generate ATS compatibility score
* Visual score representation

### 🧠 Skill Extraction

* Detect skills such as:

  * Python
  * Java
  * SQL
  * Machine Learning
  * Deep Learning
  * NLP
  * Data Analysis
  * Flask
  * MySQL

### 💡 Resume Improvement Suggestions

* Missing skills detection
* Resume enhancement recommendations
* Career readiness insights

### 📊 Resume vs Job Description Matching

* Upload Resume + JD
* Calculate similarity score using TF-IDF and Cosine Similarity
* Show:

  * Matched Skills
  * Missing Skills
  * Match Percentage

### 💼 Job Recommendations

* Fetch real-time remote jobs
* Display:

  * Job Title
  * Company Name
  * Application Link

### 📚 Learning Recommendations

* LeetCode Practice Paths
* HackerRank Challenges
* GeeksforGeeks Learning Resources
* Skill-based learning suggestions

### 🗄️ Resume History

* Store previous analyses in MySQL
* Track ATS scores over time
* View uploaded resume history

### 📈 Dashboard

* Resume analytics
* ATS insights
* Career guidance
* Learning roadmap

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript

### Backend

* Python
* Flask
* Flask-CORS

### Database

* MySQL

### Machine Learning & NLP

* Scikit-Learn
* TF-IDF Vectorizer
* Cosine Similarity
* FlashText

### PDF Processing

* PyPDF2

### APIs

* Remotive Jobs API

---

## 📂 Project Structure

```text
ResumeAnalyzer/
│
├── app.py
│
├── templates/
│   ├── index.html
│   ├── history.html
│   └── jd_match.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── uploads/
│
└── database.sql
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

### 2. Install Dependencies

```bash
pip install flask flask-cors pymysql PyPDF2 flashtext requests scikit-learn pandas
```

### 3. Configure MySQL

Create database:

```sql
CREATE DATABASE resume_analyzer;
```

Import:

```sql
USE resume_analyzer;
```

Run the SQL script provided in `database.sql`.

### 4. Configure Database Credentials

Inside `app.py`:

```python
db = pymysql.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="resume_analyzer"
)
```

### 5. Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:8080
```

---

## 📸 System Workflow

```text
Upload Resume
      ↓
Extract Text
      ↓
Extract Skills
      ↓
Calculate ATS Score
      ↓
Generate Suggestions
      ↓
Match with Job Description
      ↓
Recommend Jobs
      ↓
Recommend Learning Resources
```

---

## 🎯 Future Enhancements

* AI-powered Resume Builder
* Interview Question Generator
* Skill Gap Analysis
* Job Market Trend Analysis
* User Authentication System
* Resume Ranking System
* LinkedIn Profile Analyzer
* Interactive Analytics Dashboard
* Cloud Deployment

---

## 👨‍💻 Author

**Sridharan T R**
B.Tech Artificial Intelligence & Data Science

---

## ⭐ Project Highlights

* Full Stack Development
* Machine Learning Integration
* Resume Intelligence System
* Career Guidance Platform
* Real-Time Job Recommendations
* ATS Optimization Tool

If you found this project useful, consider giving it a ⭐ on GitHub!
