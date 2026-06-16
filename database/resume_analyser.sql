DROP DATABASE IF EXISTS resume_analyzer;

CREATE DATABASE resume_analyzer;

USE resume_analyzer;

-- =====================================
-- RESUMES TABLE
-- =====================================

CREATE TABLE resumes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    filename VARCHAR(255) NOT NULL,
    skills TEXT,
    ats_score INT,
    suggestions TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================
-- JD MATCHING HISTORY
-- =====================================

CREATE TABLE jd_matches (
    id INT AUTO_INCREMENT PRIMARY KEY,
    resume_name VARCHAR(255),
    jd_name VARCHAR(255),
    match_score FLOAT,
    matched_skills TEXT,
    missing_skills TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================
-- JOB SEARCH HISTORY
-- =====================================

CREATE TABLE job_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    job_title VARCHAR(255),
    company VARCHAR(255),
    source VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================
-- DASHBOARD STATS
-- =====================================

CREATE TABLE dashboard_stats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    total_resumes INT DEFAULT 0,
    average_ats FLOAT DEFAULT 0,
    total_jd_matches INT DEFAULT 0,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================
-- ACTIVITY LOGS
-- =====================================

CREATE TABLE activity_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    activity VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================
-- INITIAL DASHBOARD DATA
-- =====================================

INSERT INTO dashboard_stats (
    total_resumes,
    average_ats,
    total_jd_matches
)
VALUES (
    0,
    0,
    0
);

-- =====================================
-- VERIFY TABLES
-- =====================================

SHOW TABLES;