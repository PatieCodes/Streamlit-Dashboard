import streamlit as st

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="HBR - UBER Case Study Dashboard",
    layout="wide"
)

# -------------------------
# HEADER WITH LOGOS + TITLE
# -------------------------

# Layout with 3 columns for left logo, title, right logo
col1, col2, col3 = st.columns([1, 4, 1])

with col1:
    st.image("Data files/Uber-logo.png", use_container_width=True)  # Replace with your logo filename

with col2:
    st.markdown(
        """
        <h1 style='text-align: center; margin-top: 20px;'>
            HBR - UBER Case Study Dashboard
        </h1>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.image("Data files/rice-logo.jpg", use_container_width=True)  # Replace with your logo filename

st.markdown("---")  # Divider line

# -------------------------
# TABS
# -------------------------

tab1, tab2, tab3 = st.tabs(["📄 Metadata", "📘 Data Dictionary", "📊 Visualizations"])

# -------------------------
# TAB 1: METADATA
# -------------------------
with tab1:
    st.header("Metadata")
    st.write("""
    This dashboard is built to analyze the **HBR - UBER Case Study** dataset.
    
    **Includes:**
    - Dataset description  
    - Source information  
    - Purpose of analysis  
    - Notes on data quality  
    """)

# -------------------------
# TAB 2: DATA DICTIONARY
# -------------------------
with tab2:
    st.header("Data Dictionary")
    st.write("""
    Here you can list definitions of each column in the dataset.

    **Example:**
    - `timestamp`: Date and time of the ride  
    - `distance`: Trip distance in miles  
    - `fare_amount`: Total fare charged  
    - `pickup_location`: Where the ride started  
    - `dropoff_location`: Where the ride ended  
    """)

# -------------------------
# TAB 3: VISUALIZATIONS
# -------------------------
with tab3:
    st.header("Visualizations")
