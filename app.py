
import streamlit as st
import pandas as pd
from datetime import datetime
from fleet_data import initialize_fleet_data

st.set_page_config(layout="wide", page_title="Fleet Scenario Dashboard")

# Başlangıç datası
if 'fleet_df' not in st.session_state:
    st.session_state.fleet_df = initialize_fleet_data()

# Sol panel sekmeleri
selected_tab = st.sidebar.radio("📂 Navigation", [
    "📋 Table Overview",
    "⚙️ Scenario Generation",
    "📈 Fleet Avg Age Evolution - 10Y",
    "📊 Fleet Breakdown",
    "🔁 Reset",
    "📥 Download",
    "💾 Save"
])

# Table Overview sekmesi
if selected_tab == "📋 Table Overview":
    st.title("📋 Current Fleet Table")
    display_df = st.session_state.fleet_df[[
        "Reg", "MSN", "AC Type", "DOM", "DOI", "DOE", "Lease Type", "Lease End"
    ]]
    st.dataframe(display_df, use_container_width=True)


elif selected_tab == "🔁 Reset":
    st.title("🔁 Reset Fleet Data")
    if st.button("Reset to Original"):
        st.session_state.fleet_df = initialize_fleet_data()
        st.success("Fleet data has been reset to original values.")

elif selected_tab == "📥 Download":
    st.title("📥 Download Fleet Data")
    download_df = st.session_state.fleet_df.copy()
    download_df["DOM"] = download_df["DOM"].dt.strftime("%Y-%m-%d")
    download_df["DOI"] = download_df["DOI"].dt.strftime("%Y-%m-%d")
    download_df["DOE"] = download_df["DOE"].dt.strftime("%Y-%m-%d")
    download_df["Lease End"] = download_df["Lease End"].dt.strftime("%Y-%m-%d")
    csv = download_df.to_csv(index=False).encode("utf-8")
    st.download_button("Download CSV", csv, "fleet_scenario.csv", "text/csv")

elif selected_tab == "💾 Save":
    st.title("💾 Save Fleet Data")
    save_df = st.session_state.fleet_df.copy()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"fleet_saved_{timestamp}.csv"
    save_df.to_csv(f"/mnt/data/{filename}", index=False)
    st.success(f"Saved scenario as {filename}")
    st.download_button("Download Saved File", save_df.to_csv(index=False).encode("utf-8"), file_name=filename, mime="text/csv")
