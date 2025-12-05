import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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
# LOAD DATA FUNCTION
# -------------------------

data_url = 'https://docs.google.com/spreadsheets/d/1fTpJACr1Ay6DEIgFxjFZF8LgEPiwwAFY/edit?usp=sharing&ouid=103457517634340619188&rtpof=true&sd=true'

def load_file(data_url):
    # Modify URL to allow pandas to read the Excel export
    modified_url = data_url.replace('/edit?usp=sharing', '/export?format=xlsx')

    # Load ALL sheets into a dictionary
    all_sheets = pd.read_excel(modified_url, sheet_name=None)

    data = {}
    for sheet_name, df in all_sheets.items():
        data[sheet_name] = df

    return data

# Load the dataset
data = load_file(data_url)

# -------------------------
# Helper function for table display
# -------------------------
def load_data(data):
    # Show the Switchbacks dataframe
    st.dataframe(data['Switchbacks'])

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

    Below is automatically generated metadata based on the Google Sheets workbook.
    """)

    st.markdown("### 📁 Dataset Structure")

    # Show available sheets
    st.write("**Sheets Loaded:**")
    st.write(list(data.keys()))

    st.markdown("---")

    st.markdown("### 📊 Sheet Details")

    # Loop through each sheet and show metadata
    for sheet_name, df in data.items():
        with st.expander(f"📌 {sheet_name}"):
            st.write(f"**Rows:** {df.shape[0]}")
            st.write(f"**Columns:** {df.shape[1]}")
            st.write("**Column Names:**")
            st.write(list(df.columns))

            # Optional: preview first lines
            st.write("**Preview:**")
            st.dataframe(df.head())

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

    # Create 3 columns
    col_left, col_middle, col_right = st.columns([2, 2, 2])

    # LEFT COLUMN: Data + Slider filter
    with col_left:
        st.subheader("Switchbacks Table")

        df = data['Switchbacks']

        # Slider to filter rows by index
        min_row, max_row = st.slider(
            "Select row range:",
            min_value=0,
            max_value=len(df) - 1,
            value=(0, len(df) - 1)
        )

        # Filter dataframe
        filtered_df = df.iloc[min_row:max_row + 1]

        # Display filtered dataframe
        st.dataframe(filtered_df)

    # MIDDLE COLUMN (empty for now)
    with col_middle:
        st.subheader("Plot Area 1")
        st.write("Add charts here later.")

    # RIGHT COLUMN (empty for now)
    with col_right:
        st.subheader("Plot Area 2")
        st.write("Add charts here later.")
