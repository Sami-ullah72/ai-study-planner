from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "AI Study Planner Backend Running!"

@app.route('/generate-plan', methods=['POST'])
def generate_plan():
    data = request.json
    
    subjects = data.get('subjects')
    hours_per_day = data.get('hours_per_day')
    days = data.get('days')

    
    plan = {}

    for subject in subjects:
        plan[subject] = round(hours_per_day / len(subjects), 2)

    return jsonify(plan)

if __name__ == '__main__':
    app.run(debug=True)