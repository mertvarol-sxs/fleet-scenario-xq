
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
from fleet_data import initialize_fleet_data

st.set_page_config(layout="wide")

# Session state verisi
if "fleet_df" not in st.session_state:
    st.session_state.fleet_df = initialize_fleet_data()

# Sayfa navigasyonu
menu = st.sidebar.radio("Navigation", [
    "📋 Table Overview",
    "⚙️ Scenario Generation",
    "📈 Fleet Avg Age Evolution - 10Y",
    "📊 Fleet Breakdown",
    "🔁 Reset",
    "💾 Save",
    "⬇️ Download"
])

df = st.session_state.fleet_df

if menu == "📋 Table Overview":
    st.subheader("Full Fleet Table")
    st.dataframe(df, use_container_width=True)

elif menu == "⚙️ Scenario Generation":
    st.subheader("Scenario Generator")
    st.write("💡 Add or remove aircraft to simulate future scenarios.")
    st.info("Bu ekran daha sonra geliştirilecek.")

elif menu == "📈 Fleet Avg Age Evolution - 10Y":
    st.subheader("Fleet Age Projection (2025–2035)")

    def calculate_avg_age_by_year(df, years=11, start_year=2025):
        avg_ages = {}
        for year in range(start_year, start_year + years):
            date = datetime(year, 1, 1)
            active = df[(df["DOI"] <= date) & ((df["DOE"].isna()) | (df["DOE"] > date))]
            if not active.empty:
                ages = (date - active["DOM"]).dt.days / 365.25
                avg_ages[year] = ages.mean()
            else:
                avg_ages[year] = 0
        return pd.Series(avg_ages)

    base_df = initialize_fleet_data()
    base_age = calculate_avg_age_by_year(base_df)
    scen_age = calculate_avg_age_by_year(df)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=base_age.index, y=base_age.values, name="Original Fleet", mode='lines+markers'))
    fig.add_trace(go.Scatter(x=scen_age.index, y=scen_age.values, name="Scenario Fleet", mode='lines+markers'))
    fig.update_layout(title="Average Fleet Age (2025–2035)", xaxis_title="Year", yaxis_title="Avg Age (Years)")
    st.plotly_chart(fig, use_container_width=True)

elif menu == "📊 Fleet Breakdown":
    st.subheader("Fleet Breakdown")
    selected_date = st.date_input("Select Date", datetime.today())
    current = df[(df["DOI"] <= selected_date) & ((df["DOE"].isna()) | (df["DOE"] > selected_date))]

    if current.empty:
        st.warning("No active aircraft on this date.")
    else:
        st.subheader("Aircraft Type")
        fig1 = go.Figure(data=[go.Pie(labels=current["AC Type"].value_counts().index,
                                      values=current["AC Type"].value_counts().values, hole=0.4)])
        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("Lease Type")
        fig2 = go.Figure(data=[go.Pie(labels=current["Lease Type"].value_counts().index,
                                      values=current["Lease Type"].value_counts().values, hole=0.4)])
        st.plotly_chart(fig2, use_container_width=True)

elif menu == "🔁 Reset":
    st.session_state.fleet_df = initialize_fleet_data()
    st.success("Fleet reset to original state.")

elif menu == "⬇️ Download":
    st.download_button("Download Current Fleet as Excel", df.to_excel(index=False), file_name="fleet_scenario.xlsx")

elif menu == "💾 Save":
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    df.to_csv(f"fleet_saved_{timestamp}.csv", index=False)
    st.success(f"Saved current fleet as fleet_saved_{timestamp}.csv")
