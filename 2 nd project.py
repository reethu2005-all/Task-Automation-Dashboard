import streamlit as st
import os
import psutil
import pandas as pd
from datetime import datetime

# ------------------ FUNCTIONS ------------------

def get_system_info():
    return {
        "CPU Usage (%)": psutil.cpu_percent(),
        "RAM Usage (%)": psutil.virtual_memory().percent,
        "Disk Usage (%)": psutil.disk_usage('/').percent
    }

def list_files(directory):
    return os.listdir(directory)

# ------------------ STREAMLIT UI ------------------

st.set_page_config(page_title="Task Automation Dashboard", layout="centered")

st.title("⚙️ Task Automation Dashboard")
st.write("Automate and monitor basic system tasks from one dashboard.")

task = st.selectbox(
    "Select Task",
    [
        "View System Information",
        "List Files in a Directory",
        "Generate Task Report"
    ]
)

if task == "View System Information":
    st.subheader("🖥️ System Information")
    info = get_system_info()
    for key, value in info.items():
        st.write(f"**{key}:** {value}")

elif task == "List Files in a Directory":
    st.subheader("📁 Directory File Listing")
    directory = st.text_input("Enter Directory Path", "C:/")
    if st.button("Show Files"):
        if os.path.exists(directory):
            files = list_files(directory)
            st.write(files)
        else:
            st.error("Invalid directory path")

elif task == "Generate Task Report":
    st.subheader("📄 Task Automation Report")
    report = {
        "Date": datetime.now().strftime("%Y-%m-%d"),
        "Time": datetime.now().strftime("%H:%M:%S"),
        "CPU Usage (%)": psutil.cpu_percent(),
        "RAM Usage (%)": psutil.virtual_memory().percent
    }

    df = pd.DataFrame([report])
    st.table(df)

    if st.button("Save Report"):
        df.to_csv("task_report.csv", index=False)
        st.success("✅ Report saved as task_report.csv")
