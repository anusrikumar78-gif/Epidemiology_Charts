
import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os

# --------------------------------------------------
# Backend connection
# --------------------------------------------------

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from backend.data_processing import load_data
from backend.analysis import (
    total_cases,
    total_deaths
)

# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Epidemiology Trends",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# Custom CSS
# --------------------------------------------------

st.markdown(
    """
    <style>
    .main-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .sub-title {
        font-size: 18px;
        text-align: center;
        margin-bottom: 30px;
    }

    .section-title {
        font-size: 25px;
        font-weight: 600;
        margin-top: 25px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Title
# --------------------------------------------------

st.markdown(
    '<div class="main-title">📊 Epidemiology Trends in Interactive Charts</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Explore disease trends across years, age groups, genders and regions.</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# Load dataset
# --------------------------------------------------

df = load_data()

# --------------------------------------------------
# Sidebar Filters
# --------------------------------------------------

with st.sidebar:

    st.header("🎛️ Dashboard Filters")

    selected_disease = st.selectbox(
        "🦠 Select Disease",
        sorted(df["Disease"].unique())
    )

    selected_year = st.selectbox(
        "📅 Select Year",
        ["All"] + sorted(df["Year"].unique().tolist())
    )

    selected_gender = st.selectbox(
        "👤 Select Gender",
        ["All"] + sorted(df["Gender"].unique().tolist())
    )

    selected_region = st.selectbox(
        "🌍 Select Region",
        ["All"] + sorted(df["Region"].unique().tolist())
    )

# --------------------------------------------------
# Apply Filters
# --------------------------------------------------

filtered_df = df[
    df["Disease"] == selected_disease
]

if selected_year != "All":
    filtered_df = filtered_df[
        filtered_df["Year"] == selected_year
    ]

if selected_gender != "All":
    filtered_df = filtered_df[
        filtered_df["Gender"] == selected_gender
    ]

if selected_region != "All":
    filtered_df = filtered_df[
        filtered_df["Region"] == selected_region
    ]

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------

st.markdown(
    '<div class="section-title">📌 Overview</div>',
    unsafe_allow_html=True
)

case_value = total_cases(filtered_df)
death_value = total_deaths(filtered_df)
disease_count = filtered_df["Disease"].nunique()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🧮 Total Cases",
        f"{case_value:,}"
    )

with col2:
    st.metric(
        "⚠️ Total Deaths",
        f"{death_value:,}"
    )

with col3:
    st.metric(
        "🦠 Disease",
        disease_count
    )

# --------------------------------------------------
# Dataset Table
# --------------------------------------------------

st.markdown(
    '<div class="section-title">📋 Disease Dataset</div>',
    unsafe_allow_html=True
)

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

# --------------------------------------------------
# Cases Trend
# --------------------------------------------------

st.markdown(
    '<div class="section-title">📈 Disease Cases Trend</div>',
    unsafe_allow_html=True
)

disease_cases = (
    filtered_df
    .groupby(["Year", "Disease"])["Cases"]
    .sum()
    .reset_index()
)

fig_cases = px.line(
    disease_cases,
    x="Year",
    y="Cases",
    color="Disease",
    markers=True,
    title="Disease Cases Over the Years"
)

fig_cases.update_layout(
    hovermode="x unified"
)

st.plotly_chart(
    fig_cases,
    use_container_width=True
)

# --------------------------------------------------
# Deaths Comparison
# --------------------------------------------------

st.markdown(
    '<div class="section-title">📊 Disease Deaths Comparison</div>',
    unsafe_allow_html=True
)

death_data = (
    filtered_df
    .groupby(["Year", "Disease"])["Deaths"]
    .sum()
    .reset_index()
)

fig_deaths = px.bar(
    death_data,
    x="Year",
    y="Deaths",
    color="Disease",
    title="Disease Deaths Over the Years",
    text_auto=True
)

st.plotly_chart(
    fig_deaths,
    use_container_width=True
)

# --------------------------------------------------
# Age Group Analysis
# --------------------------------------------------

st.markdown(
    '<div class="section-title">👥 Cases by Age Group</div>',
    unsafe_allow_html=True
)

age_data = (
    filtered_df
    .groupby("Age_Group")["Cases"]
    .sum()
    .reset_index()
)

fig_age = px.bar(
    age_data,
    x="Age_Group",
    y="Cases",
    title="Cases by Age Group",
    text_auto=True
)

st.plotly_chart(
    fig_age,
    use_container_width=True
)

# --------------------------------------------------
# Gender Analysis
# --------------------------------------------------

st.markdown(
    '<div class="section-title">👩‍🦱👨‍🦱 Cases by Gender</div>',
    unsafe_allow_html=True
)

gender_data = (
    filtered_df
    .groupby("Gender")["Cases"]
    .sum()
    .reset_index()
)

fig_gender = px.pie(
    gender_data,
    names="Gender",
    values="Cases",
    title="Cases Distribution by Gender"
)

st.plotly_chart(
    fig_gender,
    use_container_width=True
)

# --------------------------------------------------
# Region Analysis
# --------------------------------------------------

st.markdown(
    '<div class="section-title">🌍 Cases by Region</div>',
    unsafe_allow_html=True
)

region_data = (
    filtered_df
    .groupby("Region")["Cases"]
    .sum()
    .reset_index()
)

fig_region = px.bar(
    region_data,
    x="Region",
    y="Cases",
    title="Cases by Region",
    text_auto=True
)

st.plotly_chart(
    fig_region,
    use_container_width=True
)

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Epidemiology Trends in Interactive Charts | "
    "Developed using Python, Streamlit, Pandas and Plotly"
)
# --------------------------------------------------
# About Project
# --------------------------------------------------

st.markdown("---")

st.subheader("ℹ️ About the Project")

st.write(
    """
    Epidemiology Trends in Interactive Charts is an interactive
    web-based dashboard developed to explore disease trends.

    Users can select a disease, year, gender and region to analyze
    disease cases and deaths through interactive charts.

    The project uses Python, Streamlit, Pandas and Plotly for
    data processing, analysis and visualization.
    """
)

with st.expander("🛠️ Technologies Used"):
    st.write(
        """
        • Python
        • Streamlit
        • Pandas
        • Plotly
        • CSV Dataset
        """
    )

with st.expander("🚀 Future Enhancements"):
    st.write(
        """
        • Real-time disease data integration
        • More diseases and regions
        • Disease prediction using Machine Learning
        • Cloud deployment
        • Advanced analytics
        """
    )