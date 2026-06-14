import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Progress Dashboard")

st.title("📈 Fitness Progress Dashboard")

weight = st.number_input(
    "Current Weight (kg)",
    30.0,
    200.0,
    60.0
)

water = st.number_input(
    "Water Intake (Litres)",
    0.0,
    10.0,
    2.0
)

workout_done = st.checkbox("Workout Completed Today")

if st.button("Save Progress"):

    new_data = pd.DataFrame({
        "Weight":[weight],
        "Water":[water],
        "Workout":[workout_done]
    })

    if os.path.exists("progress.csv"):
        old = pd.read_csv("progress.csv")
        data = pd.concat([old,new_data])
    else:
        data = new_data

    data.to_csv(
        "progress.csv",
        index=False
    )

    st.success("Progress Saved!")

if os.path.exists("progress.csv"):

    data = pd.read_csv("progress.csv")

    st.subheader("Weight Progress")

    fig = px.line(
        data,
        y="Weight"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Water Intake")

    fig2 = px.bar(
        data,
        y="Water"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )