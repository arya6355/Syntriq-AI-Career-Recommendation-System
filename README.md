# Syntriq AI Career Recommendation System

## Overview

The Syntriq AI Career Recommendation System is an AI-powered web application that helps users discover suitable career paths based on their skills. The system analyzes user-entered skills and recommends careers, projects, internships, certifications, learning resources, and skill improvements.

The project uses Machine Learning techniques such as TF-IDF Vectorization and Cosine Similarity to match user skills with predefined career profiles.

---

## Features

* AI-Based Career Recommendation
* Skill Gap Analysis
* Internship Recommendations
* Project Recommendations
* Career Roadmaps
* Certification Suggestions
* Learning Resource Suggestions
* Interactive React Frontend
* Flask REST API Backend

---

## Technology Stack

### Frontend

* React.js
* Axios
* CSS

### Backend

* Python
* Flask
* Flask-CORS

### Machine Learning

* Scikit-Learn
* TF-IDF Vectorizer
* Cosine Similarity

### Data Processing

* Pandas

---

## Project Structure

Syntriq-AI-Career-Recommendation-System

├── backend

│ ├── app.py

│ ├── recommender.py

│ ├── skill_gap.py

│ ├── dataset/

│ └── career_data.csv

├── frontend

│ ├── src/

│ ├── public/

│ └── package.json

└── README.md

---

## How It Works

1. User enters their skills.
2. Skills are processed using TF-IDF Vectorization.
3. Cosine Similarity calculates the closest matching career profile.
4. The system recommends:

   * Career Path
   * Projects
   * Internships
   * Certifications
   * Learning Resources
   * Career Roadmap
5. Skill Gap Analysis identifies missing skills required for the recommended career.

---

## Installation

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend Setup

```bash
cd frontend
npm install
npm start
```

---

## Sample Input

Python Machine Learning

### Sample Output

Career: ML Engineer

Project: Image Captioning

Internship: AI Intern

Certification: IBM Data Science

Skill Gap Analysis: TensorFlow

---

## Future Enhancements

* Resume Analyzer
* AI Career Chatbot
* LinkedIn Profile Analysis
* Job Recommendation Engine
* Personalized Learning Paths

---

## Author

Arya Anand

Computer Science Engineering Student

Built as part of the Syntriq AI Internship Program.
