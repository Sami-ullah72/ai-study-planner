# scheduler.py

def generate_study_plan(subjects, hours_per_day, days):
    total_difficulty = sum(subjects.values())

    plan = {}

    # Calculate hours per subject based on difficulty
    for subject, difficulty in subjects.items():
        weight = difficulty / total_difficulty
        plan[subject] = round(weight * hours_per_day, 2)

    # Create day-wise schedule
    timetable = {}

    for day in range(1, days + 1):
        timetable[f"Day {day}"] = plan

    return timetable