from utils import plot_data

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set page config for a modern look
st.set_page_config(
    page_title="Interactive Data Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("📊 Interactive Data Dashboard")
st.markdown("""
Welcome to this dynamic dashboard built with Streamlit.
Use the controls in the sidebar to customize your visualization.
""")

@st.cache_data
def load_data(num_rows):
    """Simulate data loading and processing with placeholder data."""
    np.random.seed(42)
    dates = pd.date_range(start='2022-01-01', periods=num_rows)
    data = pd.DataFrame({
        "Date": dates,
        "Category": np.random.choice(['A', 'B', 'C'], size=num_rows),
        "Value1": np.random.randn(num_rows).cumsum() + 50,
        "Value2": np.random.rand(num_rows) * 100,
        "Value3": np.random.randint(1, 10, size=num_rows),
    })
    return data

# Sidebar controls
st.sidebar.header("Customization Panel")

num_rows = st.sidebar.slider("Number of Data Points", min_value=50, max_value=1000, value=200, step=50)
data = load_data(num_rows)

category_filter = st.sidebar.multiselect(
    label="Select Categories",
    options=data['Category'].unique(),
    default=data['Category'].unique().tolist(),
)

value_to_plot = st.sidebar.selectbox(
    "Select Value to Plot",
    options=["Value1", "Value2", "Value3"],
    index=0,
)

plot_type = st.sidebar.radio(
    "Select Plot Type",
    options=["Line Chart", "Bar Chart", "Scatter Plot"],
    index=0,
)

show_moving_avg = st.sidebar.checkbox("Show 7-day Moving Average", value=True)

# Filter data based on category selection
filtered_data = data[data['Category'].isin(category_filter)]

st.subheader(f"Visualization of {value_to_plot} by Date")


plot_data(filtered_data, value_to_plot, plot_type, show_moving_avg)

# Additional Insights Section
st.markdown("---")
st.header("📈 Summary Statistics")
summary = filtered_data[value_to_plot].describe().to_frame()
st.table(summary.style.format("{:.2f}"))

st.markdown("""
---
Built with ❤️ using Streamlit
""")


# Deployment Instructions
st.sidebar.markdown("""
### Deployment Instructions
1. Create a new repository on GitHub.
2. Push your code to the repository.
3. Go to [Streamlit Community Cloud](https://streamlit.io/cloud).
4. Connect your GitHub account and select the repository.
5. Click on "Deploy".
""")
