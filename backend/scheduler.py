import random

def generate_study_plan(subjects, hours_per_day, days):
    total_difficulty = sum(subjects.values())

    # Calculate base hours per subject
    subject_hours = {}
    for subject, difficulty in subjects.items():
        weight = difficulty / total_difficulty
        subject_hours[subject] = round(weight * hours_per_day, 2)

    subject_list = list(subjects.keys())
    timetable = {}

    for day in range(1, days + 1):
        random.shuffle(subject_list)

        # Pick 2–3 subjects per day
        selected = subject_list[:min(3, len(subject_list))]

        day_plan = {}
        total_selected_difficulty = sum(subjects[s] for s in selected)

        for s in selected:
            weight = subjects[s] / total_selected_difficulty
            day_plan[s] = round(weight * hours_per_day, 2)

        timetable[f"Day {day}"] = day_plan

    return timetable