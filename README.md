<div align="center">

# 🏋️ FitGenAI — AI-Powered Personalized Workout & Diet Planner

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=40&pause=1000&color=22C55E&center=true&vCenter=true&width=900&lines=AI+Fitness+Coach;Personalized+Workout+Planner;Smart+Diet+Generator;BMI+%7C+BMR+%7C+Nutrition+Analysis" alt="Typing SVG" />

<br>

![GitHub Repo Stars](https://img.shields.io/github/stars/Mohammed-Saad-786/FitGenAI?style=for-the-badge)
![GitHub Forks](https://img.shields.io/github/forks/Mohammed-Saad-786/FitGenAI?style=for-the-badge)
![GitHub Issues](https://img.shields.io/github/issues/Mohammed-Saad-786/FitGenAI?style=for-the-badge)
![GitHub Last Commit](https://img.shields.io/github/last-commit/Mohammed-Saad-786/FitGenAI?style=for-the-badge)
![GitHub Top Language](https://img.shields.io/github/languages/top/Mohammed-Saad-786/FitGenAI?style=for-the-badge&color=yellow)
![License](https://img.shields.io/github/license/Mohammed-Saad-786/FitGenAI?style=for-the-badge)

<br>

![Fitness](https://img.shields.io/badge/Fitness-AI%20Coach-success?style=for-the-badge&logo=fitbit)
![Workout](https://img.shields.io/badge/Workout-Personalized-orange?style=for-the-badge&logo=adidas)
![Nutrition](https://img.shields.io/badge/Nutrition-Diet%20Planner-green?style=for-the-badge&logo=googlefit)
![BMI](https://img.shields.io/badge/BMI-Calculator-blue?style=for-the-badge)
![BMR](https://img.shields.io/badge/BMR-Analysis-purple?style=for-the-badge)
![AI Powered](https://img.shields.io/badge/AI-Groq-red?style=for-the-badge)

</div>

---

# 🌟 About FitGenAI

**FitGenAI** is an **AI-powered personalized fitness assistant** designed to help users achieve their health goals through intelligent workout planning, nutrition guidance, and health analysis.

Using your **age, gender, height, weight, activity level, dietary preferences, fitness goals, budget, and available equipment**, FitGenAI generates a customized fitness roadmap powered by **Groq LLMs** and **LangChain**.

Whether your goal is **weight loss**, **muscle gain**, **maintaining fitness**, or **improving overall health**, FitGenAI delivers a personalized experience tailored specifically for you.

---

# 💡 Why FitGenAI?

Unlike traditional calorie calculators or workout generators, FitGenAI combines **AI reasoning**, **health calculations**, and **Retrieval-Augmented Generation (RAG)** to provide intelligent, context-aware recommendations.

### ✨ Key Highlights

- 🤖 AI-generated workout plans
- 🥗 Personalized diet recommendations
- 📊 BMI & BMR analysis
- 🔥 Daily calorie calculation
- 💪 Protein intake recommendations
- 💧 Water intake tracker
- 🏠 Home & Gym workout support
- 💰 Budget-friendly meal planning
- 🧠 Context-aware AI responses
- ⚡ Modern Streamlit dashboard

---

# ✨ Features

## 🏋️ Personalized Workout Plans

- AI-generated exercise routines
- Beginner to advanced workouts
- Home & Gym compatibility
- Equipment-aware recommendations
- Goal-specific training plans

---

## 🥗 Smart Diet Planner

- Personalized meal plans
- Vegetarian & Non-Vegetarian support
- Budget-friendly diet suggestions
- Daily nutrition recommendations
- Protein intake optimization

---

## 📊 Health Analysis

- BMI Calculator
- BMR Calculator
- Daily calorie estimation
- Protein requirement calculation
- Body metrics analysis

---

## 💧 Hydration Tracker

- Daily water intake recommendation
- Activity-based hydration calculation

---

## 🤖 AI Fitness Coach

Powered by **Groq + LangChain**

Generates:

- Workout plans
- Meal plans
- Recovery suggestions
- Health advice
- Fitness guidance

---

## 📱 Interactive Dashboard

- Clean UI
- Responsive design
- Beautiful charts
- Easy navigation
- Real-time calculations

---

# 🛠️ Tech Stack

<div align="center">

| Category | Technologies |
|-----------|--------------|
| **Frontend** | Streamlit |
| **Programming Language** | Python |
| **LLM** | Groq |
| **Framework** | LangChain |
| **Embeddings** | Sentence Transformers |
| **Vector Database** | FAISS |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Plotly |
| **Environment** | python-dotenv |

</div>

---

# 🧠 AI Workflow

```text
User Inputs
      │
      ▼
Health Analysis
(BMI • BMR • Calories • Protein)
      │
      ▼
LangChain
      │
      ▼
Groq LLM
      │
      ▼
AI Workout Generator
      │
      ▼
AI Diet Planner
      │
      ▼
Personalized Fitness Plan
```

---

# 📊 Health Metrics Calculated

FitGenAI automatically calculates:

- ✅ Body Mass Index (BMI)
- ✅ Basal Metabolic Rate (BMR)
- ✅ Daily Maintenance Calories
- ✅ Target Calories
- ✅ Protein Intake
- ✅ Daily Water Intake

---



---

# 🚀 Live Demo

https://fitgenai-786.streamlit.app/

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Mohammed-Saad-786/FitGenAI.git
```

Navigate into the project

```bash
cd FitGenAI
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a **.env** file.

```env
GROQ_API_KEY=your_api_key_here
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

The application will start at

```
http://localhost:8501
```

---

# 📂 Project Structure

```text
FitGenAI/
│
├── ai/
│   ├── workout_generator.py
│   ├── diet_generator.py
│   └── prompts.py
│
├── rag/
│
├── rag_store/
│
├── data/
│
├── pages/
│
├── app.py
├── requirements.txt
├── .env
└── README.md
```

---

# 📈 Roadmap

## Completed

- [x] AI Workout Generator
- [x] AI Diet Planner
- [x] BMI Calculator
- [x] BMR Calculator
- [x] Daily Calories
- [x] Protein Calculator
- [x] Water Intake Calculator
- [x] Interactive Dashboard

## Future Improvements

- [ ] User Authentication
- [ ] PDF Fitness Reports
- [ ] Exercise Video Recommendations
- [ ] Wearable Device Integration
- [ ] Mobile App Version

---

# 🌍 Use Cases

FitGenAI is ideal for:

- 🏋️ Gym Beginners
- 💪 Fitness Enthusiasts
- 🥗 Nutrition Planning
- 🏃 Weight Loss Programs
- 🧘 Healthy Lifestyle Tracking
- 🏠 Home Workouts
- 🏆 Muscle Building
- 📚 Learning AI Fitness Applications

---

# 🤝 Contributing

Contributions are always welcome.

### Steps

```bash
Fork Repository
        ↓
Create Feature Branch
        ↓
Commit Changes
        ↓
Push to GitHub
        ↓
Open Pull Request
```

---

# 📝 License

This project is licensed under the **MIT License**.

---


---

# 📬 Contact

**Mohammed Saad**

[![GitHub](https://img.shields.io/badge/GitHub-Mohammed--Saad--786-181717?style=for-the-badge&logo=github)](https://github.com/Mohammed-Saad-786)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Mohammed%20Saad-blue?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/mohammed-saad-tech)

[![Email](https://img.shields.io/badge/Email-555mohammedsaad@gmail.com-red?style=for-the-badge&logo=gmail)](mailto:555mohammedsaad@gmail.com)

---

<div align="center">

### ⭐ If you found this project helpful, consider giving it a star!

**Built with ❤️ by Mohammed Saad**

<img src="https://capsule-render.vercel.app/api?type=waving&color=22C55E&height=120&section=footer"/>

</div>
