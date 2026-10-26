import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Amplats Piping Spec Selector",
    page_icon="🔧",
    layout="wide"
)

st.title("🔧 Amplats Piping Spec Selector")
st.markdown("Select commodity, material and other criteria to find the matching Pipe Material Specification.")

# Expanded Spec database (extracted from issued APP001 series documents)
specs = [
    {
        "Spec Code": "A2",
        "Full Spec No.": "APP001A2",
        "Commodity / Service": "Mine Water / Return Mine Water / Mill Circuit Water / Depressant / Plant Air / Dewatering Filtrate / Frother / Guar / Milk of Lime / Vacuum",
        "Material Type": "Carbon Steel",
        "Pressure / Rating": "Specified by Engineer",
        "Design Temp (°C)": "30",
        "Key Description": "CS Med WT PE scarfed / ERW; Flanged SABS 1123; CAF gaskets; various valves (gate, globe, check, butterfly, diaphragm)",
        "Notes": "General process / utility water services"
    },
    {
        "Spec Code": "A3",
        "Full Spec No.": "APP001A3",
        "Commodity / Service": "Potable Water",
        "Material Type": "Carbon Steel",
        "Pressure / Rating": "Specified by Engineer",
        "Design Temp (°C)": "30",
        "Key Description": "CS Med WT PE scarfed / ERW; Flanged SABS 1123; CAF gaskets; gate & diaphragm valves",
        "Notes": "Potable water service"
    },
    {
        "Spec Code": "A4",
        "Full Spec No.": "APP001A4",
        "Commodity / Service": "Dry Concentrate Transfer (DCT)",
        "Material Type": "Carbon Steel",
        "Pressure / Rating": "600 kPa @ 80°C / 700 kPa @ 100°C",
        "Design Temp (°C)": "100",
        "Key Description": "Sch 40 seamless ASTM A106 Gr B; special radius bends; pinch valves; epoxy coated",
        "Notes": "Concentrate transfer lines"
    },
    {
        "Spec Code": "A5",
        "Full Spec No.": "APP001A5",
        "Commodity / Service": "LPG / Fuel Gas / Natural Gas",
        "Material Type": "Carbon Steel",
        "Pressure / Rating": "800 kPa @ 100°C (MOP) / 1200 kPag",
        "Design Temp (°C)": "100",
        "Key Description": "ASTM A106 Gr B / API 5L B; Class 150 SO RF; threaded & BW fittings; CA 2.0 mm",
        "Notes": "Gas services - fire safe considerations"
    },
    {
        "Spec Code": "AA2",
        "Full Spec No.": "APP001AA2",
        "Commodity / Service": "Effluent Water (Mine) / HP Flushing Water / Mill Circuit Water / Return Dam Water / Borehole Water",
        "Material Type": "Carbon Steel",
        "Pressure / Rating": "Specified by Engineer",
        "Design Temp (°C)": "Specified",
        "Key Description": "Carbon steel piping for effluent and flushing services",
        "Notes": "Water / effluent"
    },
    {
        "Spec Code": "AA5",
        "Full Spec No.": "APP001AA5",
        "Commodity / Service": "Mine Water (Under Ground)",
        "Material Type": "Carbon Steel",
        "Pressure / Rating": "Specified by Engineer",
        "Design Temp (°C)": "Specified",
        "Key Description": "Underground mine water piping",
        "Notes": "Underground service"
    },
    {
        "Spec Code": "AF2",
        "Full Spec No.": "APP001AF2",
        "Commodity / Service": "Slurry (Drains Ug) / Service Water (Ug) / Plant Air (Ug)",
        "Material Type": "Carbon Steel",
        "Pressure / Rating": "Specified by Engineer",
        "Design Temp (°C)": "Specified",
        "Key Description": "Underground slurry, service water and plant air",
        "Notes": "Underground services"
    },
    {
        "Spec Code": "AF3",
        "Full Spec No.": "APP001AF3",
        "Commodity / Service": "Slurry (Drains Ug) / Service Water (Ug)",
        "Material Type": "Carbon Steel",
        "Pressure / Rating": "Specified by Engineer",
        "Design Temp (°C)": "Specified",
        "Key Description": "Underground slurry drains and service water",
        "Notes": "Underground services"
    },
    {
        "Spec Code": "AL2",
        "Full Spec No.": "APP001AL2",
        "Commodity / Service": "Slurry (Drain Ug) / Service Water (Ug) / Plant Air (Ug)",
        "Material Type": "Carbon Steel",
        "Pressure / Rating": "Specified by Engineer",
        "Design Temp (°C)": "Specified",
        "Key Description": "Underground slurry, service water and plant air",
        "Notes": "Underground services"
    },
    {
        "Spec Code": "AL3",
        "Full Spec No.": "APP001AL3",
        "Commodity / Service": "Slurry (Drain Ug)",
        "Material Type": "Carbon Steel",
        "Pressure / Rating": "Specified by Engineer",
        "Design Temp (°C)": "Specified",
        "Key Description": "Underground slurry drain piping",
        "Notes": "Underground slurry"
    },
    {
        "Spec Code": "B3",
        "Full Spec No.": "APP001B3",
        "Commodity / Service": "Mine Water / Service Water / Sludge/Slurry",
        "Material Type": "Carbon Steel",
        "Pressure / Rating": "Specified by Engineer",
        "Design Temp (°C)": "Specified",
        "Key Description": "ASTM A106 Gr B Sch 40 PE SMLS; flanged; gutta percha rubber gaskets; high tensile bolting",
        "Notes": "Process / slurry services"
    },
    {
        "Spec Code": "B4",
        "Full Spec No.": "APP001B4",
        "Commodity / Service": "Sludge (Ug) / Service Water (Ug) / Mine Water (Ug)",
        "Material Type": "Carbon Steel",
        "Pressure / Rating": "Specified by Engineer",
        "Design Temp (°C)": "Specified",
        "Key Description": "Underground sludge, service water and mine water",
        "Notes": "Underground services"
    },
    {
        "Spec Code": "BA",
        "Full Spec No.": "APP001BA",
        "Commodity / Service": "Cooling Water Supply / Cooling Water Return / Process Water / Fire Water / Chilled Water / Plant Air LP / Process Water",
        "Material Type": "Carbon Steel",
        "Pressure / Rating": "800 kPa(water) / 1000 kPa / 1500 kPa test",
        "Design Temp (°C)": "90",
        "Key Description": "CS ERW screwed/BW; SABS 62 / 719; Class 150; CAF/Gylon gaskets; various fittings",
        "Notes": "Cooling, fire water, process water, plant air"
    },
    {
        "Spec Code": "BB",
        "Full Spec No.": "APP001BB",
        "Commodity / Service": "Nitrogen",
        "Material Type": "Carbon Steel",
        "Pressure / Rating": "Specified by Engineer",
        "Design Temp (°C)": "Specified",
        "Key Description": "Nitrogen service piping",
        "Notes": "Nitrogen utility"
    },
    {
        "Spec Code": "E2",
        "Full Spec No.": "APP001E2",
        "Commodity / Service": "Mine Water (Ug) / Service Water (Ug) / Sludge/Slurry (Ug)",
        "Material Type": "Carbon Steel",
        "Pressure / Rating": "Specified by Engineer",
        "Design Temp (°C)": "Specified",
        "Key Description": "ASTM A106 Gr B Sch STD PE pipe; flanged specials; sleeves",
        "Notes": "Underground mine water and slurry"
    },
]

df = pd.DataFrame(specs)

# Sidebar filters
st.sidebar.header("Selection Criteria")

# Build commodity list from all entries
all_commodities = set()
for row in df["Commodity / Service"]:
    for part in row.split("/"):
        all_commodities.add(part.strip())
commodities = ["(Any)"] + sorted(all_commodities)

materials = ["(Any)"] + sorted(df["Material Type"].unique().tolist())
ratings = ["(Any)"] + sorted(df["Pressure / Rating"].unique().tolist())

selected_commodity = st.sidebar.selectbox("Commodity / Service", commodities)
selected_material = st.sidebar.selectbox("Material Type", materials)
selected_rating = st.sidebar.selectbox("Pressure / Rating", ratings)
keyword = st.sidebar.text_input("Additional Keyword (optional)")

# Filtering logic
filtered = df.copy()

if selected_commodity != "(Any)":
    filtered = filtered[filtered["Commodity / Service"].str.contains(selected_commodity, case=False, na=False)]

if selected_material != "(Any)":
    filtered = filtered[filtered["Material Type"].str.contains(selected_material, case=False, na=False)]

if selected_rating != "(Any)":
    filtered = filtered[filtered["Pressure / Rating"].str.contains(selected_rating, case=False, na=False)]

if keyword:
    mask = (
        filtered["Key Description"].str.contains(keyword, case=False, na=False) |
        filtered["Notes"].str.contains(keyword, case=False, na=False) |
        filtered["Commodity / Service"].str.contains(keyword, case=False, na=False) |
        filtered["Spec Code"].str.contains(keyword, case=False, na=False)
    )
    filtered = filtered[mask]

st.subheader("Matching Specifications")

if filtered.empty:
    st.warning("No matching specifications found. Try broadening your criteria.")
else:
    st.success(f"Found {len(filtered)} matching specification(s)")
    st.dataframe(
        filtered,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Commodity / Service": st.column_config.TextColumn(width="large"),
            "Key Description": st.column_config.TextColumn(width="large"),
        }
    )

    for _, row in filtered.iterrows():
        with st.expander(f"Spec {row['Spec Code']} — {row['Full Spec No.']}"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Material:** {row['Material Type']}")
                st.markdown(f"**Rating:** {row['Pressure / Rating']}")
                st.markdown(f"**Design Temp:** {row['Design Temp (°C)']} °C")
            with col2:
                st.markdown(f"**Notes:** {row['Notes']}")
            st.markdown("**Description:**")
            st.write(row["Key Description"])
            st.markdown("**Commodities covered:**")
            st.write(row["Commodity / Service"])

st.divider()
st.markdown("### Full Spec Database")
with st.expander("View complete database"):
    st.dataframe(df, use_container_width=True, hide_index=True)

st.caption("Based on issued Amplats (Anglo American Platinum) Pipe Material Specifications (APP001 series). Database continues to be expanded. Always verify against the full specification documents and project design basis.")
