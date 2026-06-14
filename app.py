import streamlit as st
from ai.workout_generator import generate_plan

if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

if "ai_plan" not in st.session_state:
    st.session_state.ai_plan = None


# ------------------------------
# PAGE CONFIG
# ------------------------------

st.set_page_config(
    page_title="FitGenAI",
    page_icon="💪",
    layout="wide"
)

# ------------------------------
# CUSTOM CSS
# ------------------------------

st.markdown("""
<style>

.main {
    background-color: #f8fafc;
}

.title {
    font-size: 3rem;
    font-weight: 800;
    color: #16a34a;
    text-align: center;
}

.subtitle {
    text-align:center;
    color:gray;
    font-size:18px;
    margin-bottom:30px;
}

.metric-card {
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0 4px 15px rgba(0,0,0,0.08);
    text-align:center;
}

.metric-value {
    font-size:28px;
    font-weight:bold;
    color:#16a34a;
}

.metric-label {
    color:gray;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------
# HEADER
# ------------------------------

st.markdown(
    '<p class="title">🏋️ FitGenAI</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">AI-Powered Personalized Workout & Diet Planner</p>',
    unsafe_allow_html=True
)

# ------------------------------
# USER FORM
# ------------------------------

st.header("👤 User Profile")

col1, col2 = st.columns(2)

with col1:

    name = st.text_input("Name")

    age = st.number_input(
        "Age",
        min_value=15,
        max_value=80,
        value=21
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    height = st.number_input(
        "Height (cm)",
        min_value=100,
        max_value=250,
        value=170
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=30,
        max_value=200,
        value=70
    )

with col2:

    activity = st.selectbox(
        "Activity Level",
        [
            "Sedentary",
            "Lightly Active",
            "Moderately Active",
            "Very Active"
        ]
    )

    goal = st.selectbox(
        "Fitness Goal",
        [
            "Weight Loss",
            "Muscle Gain",
            "Weight Maintenance",
            "General Fitness"
        ]
    )

    diet = st.selectbox(
        "Diet Preference",
        [
            "Vegetarian",
            "Non-Vegetarian",
            "Vegan"
        ]
    )

    budget = st.slider(
        "Daily Food Budget (₹)",
        100,
        2000,
        500
    )

    equipment = st.selectbox(
        "Available Equipment",
        [
            "None",
            "Dumbbells",
            "Resistance Bands",
            "Full Gym"
        ]
    )

# ------------------------------
# CALCULATE BUTTON
# ------------------------------


# ------------------------------
# CALCULATE BUTTON
# ------------------------------

if st.button("🚀 Generate Health Analysis"):
    st.session_state.analysis_done = True

if st.session_state.analysis_done:

    # BMI
    bmi = weight / ((height / 100) ** 2)

    if bmi < 18.5:
        bmi_category = "Underweight"
    elif bmi < 25:
        bmi_category = "Normal"
    elif bmi < 30:
        bmi_category = "Overweight"
    else:
        bmi_category = "Obese"

    # BMR
    if gender == "Male":
        bmr = (
            10 * weight +
            6.25 * height -
            5 * age +
            5
        )
    else:
        bmr = (
            10 * weight +
            6.25 * height -
            5 * age -
            161
        )

    activity_multiplier = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Moderately Active": 1.55,
        "Very Active": 1.725
    }

    calories = bmr * activity_multiplier[activity]

    if goal == "Weight Loss":
        calories -= 300
    elif goal == "Muscle Gain":
        calories += 300

    protein = round(weight * 1.6)
    water = round(weight * 0.035, 1)

    st.success("Health Analysis Generated!")

    st.header("📊 Health Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("BMI", round(bmi, 1))

    with c2:
        st.metric("Category", bmi_category)

    with c3:
        st.metric("Calories", f"{int(calories)} kcal")

    with c4:
        st.metric("Protein", f"{protein} g")

    st.metric(
        "💧 Daily Water Intake",
        f"{water} Litres"
    )

    st.header("🧠 AI Health Summary")

    st.info(
        f"""
Hello {name},

Based on your profile:

• Goal: {goal}

• Activity Level: {activity}

• Recommended Calories: {int(calories)} kcal/day

• Protein Requirement: {protein} g/day

• Water Intake: {water} L/day

• BMI Status: {bmi_category}

This information will be used to generate your personalized AI workout and diet plan.
"""
    )

    st.header("🤖 AI Personalized Fitness Plan")

    user_profile = {
        "name": name,
        "age": age,
        "height": height,
        "weight": weight,
        "goal": goal,
        "diet": diet,
        "equipment": equipment
    }

    if st.button("Generate AI Workout & Diet Plan"):

        with st.spinner("Generating personalized recommendations..."):

            st.session_state.ai_plan = generate_plan(
                user_profile
            )

    if st.session_state.ai_plan:

        st.success("Plan Generated Successfully!")

        st.markdown(
            st.session_state.ai_plan
        )

