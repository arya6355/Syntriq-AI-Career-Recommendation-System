from flask import Flask
from flask import request
from flask import jsonify

from flask_cors import CORS

from recommender import recommend_career
from skill_gap import find_missing_skills

app = Flask(__name__)

CORS(app)


@app.route("/recommend", methods=["POST"])
def recommend():

    data = request.json

    skills = data["skills"]

    result = recommend_career(skills)

    missing_skills = find_missing_skills(
        skills,
        result["Skills"]
    )

    return jsonify({

        "career": result["Career"],

        "skills": result["Skills"],

        "project": result["Projects"],

        "internship": result["Internships"],

        "roadmap": result["Roadmap"],

        "certification": result["Certification"],

        "resources": result["Resources"],

        "missing_skills": missing_skills

    })


if __name__ == "__main__":
    app.run(debug=True)     