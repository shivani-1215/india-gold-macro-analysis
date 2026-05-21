import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
master = pd.read_csv("master_clean.csv", index_col='year')
master['total_gold_demand'] = master['jewellery_demand_tonnes'] + master['bar_coin_demand_tonnes']

# App title
st.title("What If India Stopped Buying Gold?")
st.subheader("A Macroeconomic Impact Analysis — 2010 to 2024")
st.markdown("---")

# Hero metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Avg Annual Gold Demand", "800 Tonnes", "World's largest consumer")
col2.metric("Share of Trade Deficit", "~25%", "2nd largest import")
col3.metric("Rupee Change", "₹45 → ₹84", "2010 to 2024")
col4.metric("Forex Reserves", "$643B", "↑ from $300B in 2010")

st.markdown("---")
st.markdown("### India spends over $35 billion every year buying gold. This project asks — what happens if that stops?")
# Section 2 - Gold demand over time
st.markdown("---")
st.header("Section 2 — Gold Demand Over Time")

fig, ax = plt.subplots(figsize=(12, 5))
ax.bar(master.index, master['total_gold_demand'], color='#C9A84C')
ax.set_title('India Gold Demand 2010-2024 (Tonnes)')
ax.set_xlabel('Year')
ax.set_ylabel('Tonnes')
ax.grid(axis='y', alpha=0.3)
st.pyplot(fig)

st.markdown("**Key insight:** Every time India raised import duty on gold, demand fell — but always recovered within 2 years. Gold demand in India is sticky.")
# Section 3 - CAD
st.markdown("---")
st.header("Section 3 — Current Account Deficit")
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(master.index, master['cad_pct_gdp'], color='#D85A30', marker='o')
ax.set_title('CAD % of GDP 2010-2024')
ax.set_xlabel('Year')
ax.set_ylabel('CAD % of GDP')
ax.grid(alpha=0.3)
st.pyplot(fig)
st.markdown("**Key insight:** CAD hit -5% in 2012 — the worst deficit year. Gold imports were at peak that year.")

# Section 4 - Rupee
st.markdown("---")
st.header("Section 4 — Rupee Depreciation")
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(master.index, master['inr_usd_rate'], color='#185FA5', marker='o')
ax.set_title('INR per USD 2010-2024')
ax.set_xlabel('Year')
ax.set_ylabel('INR per USD')
ax.grid(alpha=0.3)
st.pyplot(fig)
st.markdown("**Key insight:** Rupee fell from ₹45 to ₹84 — nearly doubled in 15 years. CAD pressure from gold imports is a key driver.")

# Section 5 - Forex
st.markdown("---")
st.header("Section 5 — Forex Reserves")
fig, ax = plt.subplots(figsize=(12, 5))
ax.bar(master.index, master['forex_reserves_usd_bn'], color='#0F6E56')
ax.set_title('Forex Reserves USD Billion 2010-2024')
ax.set_xlabel('Year')
ax.set_ylabel('USD Billion')
ax.grid(axis='y', alpha=0.3)
st.pyplot(fig)
st.markdown("**Key insight:** Forex reserves doubled from $300B to $643B. Less gold imports means more forex saved.")

# Section 6 - Regression Findings
st.markdown("---")
st.header("Section 6 — Regression Findings")

st.markdown("### Model 1 — What drives India's CAD?")
st.markdown("**Variables used:** Gold demand, Fuel imports, GDP growth")
col1, col2, col3 = st.columns(3)
col1.metric("R-squared", "0.60", "Explains 60% of CAD")
col2.metric("Gold coefficient", "-0.014", "More gold = worse CAD")
col3.metric("Correlation", "-0.64", "Strong negative relationship")
st.markdown("**Finding:** Every 100 extra tonnes of gold demand, CAD worsens by 1.14% of GDP.")

st.markdown("---")
st.markdown("### Model 2 — What drives the Rupee?")
st.markdown("**Variables used:** CAD, Forex reserves, Gold price")
col4, col5, col6 = st.columns(3)
col4.metric("R-squared", "0.825", "Explains 82.5% of rupee movement")
col5.metric("Forex coefficient", "0.07", "More reserves = rupee weakens less")
col6.metric("CAD coefficient", "1.35", "Worse CAD = weaker rupee")
st.markdown("**Finding:** CAD and forex reserves explain 82.5% of rupee movement.")

st.markdown("---")
st.info("**The complete chain: More gold imports → Wider CAD (Model 1) → Weaker Rupee (Model 2)**")
# Section 7 - Gold circulation calculator
st.markdown("---")
st.header("Section 7 — Gold Circulation Calculator")
st.markdown("India already has enough gold. What if we used it instead of importing more?")

rbi = st.slider("% of RBI's 800 tonnes activated", 0, 40, 10)
household = st.slider("% of household 25,000 tonnes activated", 0, 10, 2)
temple = st.slider("% of temple 3,000 tonnes activated", 0, 30, 5)

rbi_tonnes = 800 * rbi / 100
household_tonnes = 25000 * household / 100
temple_tonnes = 3000 * temple / 100
total_tonnes = rbi_tonnes + household_tonnes + temple_tonnes
import_reduction_usd = total_tonnes * 0.06
cad_improvement = (import_reduction_usd / 10) * 0.35

st.metric("Total gold activated (tonnes)", f"{round(total_tonnes)} T")
st.metric("Import reduction", f"${round(import_reduction_usd, 1)}B")
st.metric("CAD improvement", f"{round(cad_improvement, 2)}% of GDP")

# Section 8 - Policy simulator
st.markdown("---")
st.header("Section 8 — Policy Simulator")
st.markdown("What if India reduced gold imports? See the impact live.")

reduction = st.slider("Gold import reduction %", 0, 100, 25)
baseline_imports = 35
saved = baseline_imports * reduction / 100
cad_impact = (saved / 10) * 0.35
rupee_impact = saved * 0.06

st.metric("Import saving", f"${round(saved, 1)}B per year")
st.metric("CAD improvement", f"{round(cad_impact, 2)}% of GDP")
st.metric("Estimated rupee strengthening", f"₹{round(rupee_impact, 1)}")
