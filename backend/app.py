from flask import Flask, request, jsonify
from flask_cors import CORS
from scheduler import generate_study_plan

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "AI Study Planner Backend Running!"

@app.route('/generate-plan', methods=['POST'])
def generate_plan():
    data = request.json

    raw_subjects = data.get('subjects')
    hours_per_day = int(data.get('hours_per_day'))
    days = int(data.get('days'))

    subjects = {}

    for item in raw_subjects:
        name, difficulty = item.split(":")
        subjects[name.strip()] = int(difficulty)

    timetable = generate_study_plan(subjects, hours_per_day, days)

    return jsonify(timetable)

if __name__ == '__main__':
    app.run(debug=True)