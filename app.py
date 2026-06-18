import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
page_title="Population Growth Dashboard",
layout="wide"
)

st.title("📈 Smart Population Growth and Migration Analysis System")

df = pd.read_csv("population_data.csv")

current_population = df["Final Population"].iloc[-1]
max_population = df["Final Population"].max()
avg_population = df["Final Population"].mean()

col1, col2, col3 = st.columns(3)

col1.metric("Current Population", f"{current_population:,.0f}")
col2.metric("Maximum Population", f"{max_population:,.0f}")
col3.metric("Average Population", f"{avg_population:,.0f}")

st.subheader("Population Growth Trend")

fig, ax = plt.subplots()
ax.plot(df["Year"], df["Final Population"])
ax.set_xlabel("Year")
ax.set_ylabel("Population")

st.pyplot(fig)

st.subheader("Population Data")
st.dataframe(df)

st.subheader("Population Query")

selected_year = st.number_input(
"Enter Year",
min_value=1,
max_value=50,
value=1
)

record = df[df["Year"] == selected_year]

if not record.empty:
  st.write(record)
