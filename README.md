# 🧠 AI Study Planner

A smart web application that generates personalized study schedules based on subject difficulty and available study time.

---

## 🚀 Features (Implemented)

* 📚 Input subjects with difficulty level
* ⏱️ Customize daily study hours
* 📅 Generate day-wise study timetable
* 🧠 Difficulty-based smart scheduling algorithm
* 🔄 Backend API integration with frontend

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python (Flask)
* **Other Tools:** REST API, JSON

---

## 📂 Project Structure

```
ai-study-planner/
│
├── frontend/
│   └── index.html
│
├── backend/
│   ├── app.py
│   └── scheduler.py
│
└── README.md
```

---

## ⚙️ How It Works

1. User enters subjects with difficulty level (1–5)
2. Provides available study hours per day and total days
3. Backend processes input using a weighted scheduling algorithm
4. Generates a structured day-wise timetable

---

## 🧪 Example Input

```
Math:3,Physics:2,DSA:5
Hours per day: 6
Days: 3
```

---

## 📊 Example Output

```

  Math: 1.8 hrs
  Physics: 1.2 hrs
  DSA: 3.0 hrs
```

(Same structure for remaining days)

---

## 🧠 Algorithm Used

* Calculates total difficulty
* Assigns weight to each subject
* Distributes study hours proportionally
* Generates a consistent daily schedule

---

## ⚠️ Known Limitations

* Same schedule repeated each day
* No topic-level planning yet
* No user authentication
* Basic UI

---

## 🔮 Future Improvements

* 📌 Topic-based planning
* 🔄 Adaptive timetable (based on progress)
* 📊 Progress tracking dashboard
* 🔐 User login system
* 🌐 Deployment on cloud (Vercel + Render)
* 🤖 AI-based recommendations

---

## ▶️ How to Run Locally

### Backend:

```bash
cd backend
pip install flask flask-cors
python app.py
```

### Frontend:

* Open `frontend/index.html` in browser

---

## 💡 Project Status

✅ Completed till: Smart scheduling (Day 2)
🚧 Next: Advanced timetable + UI improvements

---

## 👨‍💻 Author

* Sami ullah
