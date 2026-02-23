import streamlit as st

# ---------------- LOGIN CHECK ----------------

if not st.session_state.get("logged_in"):
    st.switch_page("login.py")

if st.session_state.get("user_role") != "admin":
    st.warning("Access denied. Admin only.")
    st.stop()

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("### 👤 Logged in user")
    st.write(st.session_state.get("user_email", ""))

    st.markdown("---")

    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.switch_page("login.py")



import pandas as pd
import streamlit as st
import plotly.express as px
import unicodedata

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(page_title="Training Dashboard", layout="wide")

# ==================================================
# DASHBOARD TITLE
# ==================================================
st.markdown(
    """
    <style>
    /* ===============================
       TOP STREAMLIT HEADER (ONLY)
       =============================== */

    /* Header background */
    [data-testid="stHeader"] {
        background: linear-gradient(180deg, #0B3C5D, #06283D);
    }

    /* Deploy button text */
    [data-testid="stHeader"] a {
        color: white !important;
        font-weight: 600;
    }

    /* Header buttons (rerun, menu) */
    [data-testid="stHeader"] button {
        color: white !important;
    }

    /* Header icons (three dots, rerun icon) */
    [data-testid="stHeader"] svg {
        fill: white !important;
        color: white !important;
    }

    /* Hover effect */
    [data-testid="stHeader"] a:hover,
    [data-testid="stHeader"] button:hover {
        opacity: 0.85;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>

    /* ---------------- APP BACKGROUND ---------------- */
    .stApp {
        background-color: #ADD8E6;
    }

    /* ---------------- SIDEBAR ---------------- */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0B3C5D, #07263D);
    }

    [data-testid="stSidebar"] * {
        color: white !important;
        font-weight: 500;
    }

    /* ---------------- HEADER BANNER ---------------- */
    .header-banner {
        background:
            linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)),
            url("https://ssinnovations.com/wp-content/uploads/2025/07/SSI-M3-Home-Splash-MAR25-v3.webp");
        background-size: cover;
        background-position: center;
        border-radius: 22px;
        padding: 80px 40px;
        color: white;
        text-align: center;
        margin-bottom: 50px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.25);
    }

    .header-banner h1 {
        font-size: 44px;
        font-weight: 800;
        margin-bottom: 12px;
        letter-spacing: 0.5px;
    }

    .header-banner p {
        font-size: 18px;
        max-width: 900px;
        margin: auto;
        opacity: 0.95;
    }

    /* ---------------- SECTION TITLE ---------------- */
    .section-title {
        text-align: center;
        font-size: 26px;
        font-weight: 700;
        margin-bottom: 40px;
        color: #0B3C5D;
    }

    /* ---------------- CARDS ---------------- */
    .card {
        background: #F0F8FF;
        padding: 30px;
        border-radius: 18px;
        text-align: center;
        box-shadow: 0 12px 30px rgba(0,0,0,0.10);
        height: 340px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: all 0.35s ease;
        border-top: 6px solid #1F77B4;
    }

    .card:hover {
        transform: translateY(-8px);
        box-shadow: 0 18px 45px rgba(0,0,0,0.18);
    }

    .card h3 {
        margin-bottom: 14px;
        color: #0B3C5D;
        font-weight: 700;
    }

    .card p {
        color: #555;
        font-size: 15px;
        line-height: 1.6;
    }

    /* ---------------- BUTTONS ---------------- */
    .stButton button {
        background-color: #1F77B4;
        color: white;
        border-radius: 10px;
        padding: 10px 18px;
        font-weight: 600;
        border: none;
        transition: all 0.3s ease;
    }

    .stButton button:hover {
        background-color: #155A8A;
        transform: scale(1.04);
    }

    /* ---------------- FOOTER ---------------- */
    .footer {
        text-align: center;
        color: #777;
        font-size: 13px;
        margin-top: 60px;
    }

    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>

    /* ===============================
       DARK MODE BASE
       =============================== */
    .stApp {
        background: linear-gradient(
            135deg,
            #0f2027,
            #203a43,
            #2c5364
        );
        animation: gradientMove 18s ease infinite;
        background-size: 400% 400%;
        color: #EAEAEA;
    }

    @keyframes gradientMove {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* ===============================
       HEADER BANNER
       =============================== */
    .header-banner {
        background: linear-gradient(
            rgba(0,0,0,0.65),
            rgba(0,0,0,0.65)
        ),
        url("https://ssinnovations.com/wp-content/uploads/2025/07/SSI-M3-Home-Splash-MAR25-v3.webp");
        background-size: cover;
        background-position: center;
        padding: 45px;
        border-radius: 14px;
        margin-bottom: 25px;
        text-align: center;
        color: white;
        font-size: 32px;
        font-weight: 700;
        letter-spacing: 1px;
    }

    /* ===============================
       MAIN CONTENT CARD
       =============================== */
    section[data-testid="stMain"] {
        background-color: rgba(18, 24, 38, 0.88);
        padding: 25px;
        border-radius: 16px;
    }

    /* ===============================
       KPI CARDS STYLE
       =============================== */
    div[data-testid="metric-container"] {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 14px;
        padding: 18px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.35);
    }

    /* ===============================
       MULTISELECT CHIPS
       =============================== */
    [data-testid="stMultiSelect"] span {
        background-color: #1F77B4 !important;
        color: white !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
    }

    [data-testid="stMultiSelect"] span:hover {
        background-color: #155A8A !important;
    }

    [data-testid="stMultiSelect"] svg {
        color: white !important;
    }

    /* ===============================
       LOGO WATERMARK
       =============================== */
    .watermark {
        position: fixed;
        bottom: 15px;
        right: 20px;
        opacity: 0.15;
        z-index: 0;
        pointer-events: none;
    }

    </style>

    <!-- HEADER -->
    <div class="header-banner">
        Learning & Development Dashboard
    </div>

    <!-- WATERMARK -->
    <img class="watermark"
         src="https://upload.wikimedia.org/wikipedia/commons/a/ab/Logo_TV_2015.png"
         width="120"/>

    """,
    unsafe_allow_html=True
)

# ==================================================
# GLOBAL STYLES (BACKGROUND + FILTER CHIPS + KPI CARDS)
# ==================================================
st.markdown(
    """
    <style>
    /* App background */
    .stApp {
        background-color: #F0F2F6;
    }

    /* Multiselect selected items (chips) */
    [data-testid="stMultiSelect"] span {
        background-color: #1F77B4 !important;
        color: white !important;
        font-weight: 600 !important;
        border-radius: 6px !important;
    }

    [data-testid="stMultiSelect"] svg {
        color: white !important;
    }

    [data-testid="stMultiSelect"] span:hover {
        background-color: #155A8A !important;
    }

    /* KPI cards */
    .kpi-row {
        display: flex;
        gap: 20px;
        margin-bottom: 20px;
    }

    .kpi-card {
        background: white;
        border-radius: 14px;
        padding: 20px;
        width: 100%;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }

    .kpi-title {
        font-size: 14px;
        color: #6B7280;
        margin-bottom: 6px;
    }

    .kpi-value {
        font-size: 36px;
        font-weight: 700;
        color: #111827;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==================================================
# LOAD EXCEL (ALL SHEETS)
# ==================================================
FILE = "training_data.xlsx"
xls = pd.ExcelFile(FILE)

dfs = []

for sheet in xls.sheet_names:
    temp = pd.read_excel(FILE, sheet_name=sheet, engine="openpyxl")

    temp.columns = [
        unicodedata.normalize("NFKD", str(c))
        .replace("\u00A0", "")
        .replace("\u200b", "")
        .replace("\n", "")
        .strip()
        for c in temp.columns
    ]

    required_cols = {
        "Employee",
        "Department",
        "Training_Status",
        "Assessment_Status"
    }

    if required_cols.issubset(set(temp.columns)):
        temp["Training_Name"] = sheet
        dfs.append(temp)
    else:
        st.warning(f"Skipped sheet '{sheet}' (header issue)")

if not dfs:
    st.error("No valid training sheets found in Excel.")
    st.stop()

df = pd.concat(dfs, ignore_index=True)

# ==================================================
# NORMALIZE STATUS VALUES
# ==================================================
df["Training_Status"] = df["Training_Status"].astype(str).str.strip().str.title()
df["Assessment_Status"] = df["Assessment_Status"].astype(str).str.strip().str.title()

# ==================================================
# SIDEBAR FILTERS
# ==================================================
st.sidebar.header("Filters")
st.sidebar.markdown("---")

if st.sidebar.button("🔄 Refresh Data"):
    st.rerun()

training_filter = st.sidebar.multiselect(
    "Training",
    sorted(df["Training_Name"].unique()),
    default=sorted(df["Training_Name"].unique())
)

dept_filter = st.sidebar.multiselect(
    "Department",
    sorted(df["Department"].unique()),
    default=sorted(df["Department"].unique())
)

df_filt = df[
    (df["Training_Name"].isin(training_filter)) &
    (df["Department"].isin(dept_filter))
]

# ==================================================
# KPI CALCULATIONS
# ==================================================
total_employees = df_filt["Employee"].nunique()

employees_trained = df_filt.loc[
    df_filt["Training_Status"] == "Done", "Employee"
].nunique()

training_completion_pct = round(
    (employees_trained / total_employees) * 100, 1
) if total_employees else 0

pending_trainings = (df_filt["Training_Status"] != "Done").sum()

pass_count = (df_filt["Assessment_Status"] == "Pass").sum()
fail_count = (df_filt["Assessment_Status"] == "Fail").sum()

total_attempted = pass_count + fail_count
pass_pct = round((pass_count / total_attempted) * 100, 1) if total_attempted else 0
fail_pct = round((fail_count / total_attempted) * 100, 1) if total_attempted else 0

# ==================================================
# KPI CARDS (BOXES WITH ROUNDED CORNERS)
# ==================================================
st.markdown(
    f"""
    <div class="kpi-row">
        <div class="kpi-card">
            <div class="kpi-title">Total Employees</div>
            <div class="kpi-value">{total_employees}</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-title">Employees Trained</div>
            <div class="kpi-value">{employees_trained}</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-title">Training Completion %</div>
            <div class="kpi-value">{training_completion_pct}%</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-title">Pending Trainings</div>
            <div class="kpi-value">{pending_trainings}</div>
        </div>
    </div>

    <div class="kpi-row">
        <div class="kpi-card">
            <div class="kpi-title">Pass %</div>
            <div class="kpi-value">{pass_pct}%</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-title">Fail %</div>
            <div class="kpi-value">{fail_pct}%</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ==================================================
# COLORS
# ==================================================
TRAINING_COLORS = {
    "Done": "#27AE60",
    "Not-Attended": "#E74C3C",
    "Lined-Up": "#F39C12"
}

ASSESSMENT_COLORS = {
    "Pass": "#27AE60",
    "Fail": "#E74C3C",
    "Lined-Up": "#F39C12",
    "Not Attempted": "#C8939C"
}

# ==================================================
# CHART 1: TRAINING STATUS
# ==================================================
df_chart1 = (
    df_filt.groupby(["Department", "Training_Status"])
    .size()
    .reset_index(name="Count")
)

df_chart1["Percent"] = (
    df_chart1["Count"] /
    df_chart1.groupby("Department")["Count"].transform("sum") * 100
).round(1)

fig1 = px.bar(
    df_chart1,
    x="Department",
    y="Count",
    color="Training_Status",
    text=df_chart1["Percent"].astype(str) + "%",
    color_discrete_map=TRAINING_COLORS,
    title="Department-wise Training Status (%)"
)

fig1.update_traces(textposition="inside")
st.plotly_chart(fig1, use_container_width=True)

# ==================================================
# CHART 2: ASSESSMENT RESULT
# ==================================================
df_chart2 = (
    df_filt.groupby(["Department", "Assessment_Status"])
    .size()
    .reset_index(name="Count")
)

df_chart2["Percent"] = (
    df_chart2["Count"] /
    df_chart2.groupby("Department")["Count"].transform("sum") * 100
).round(1)

fig2 = px.bar(
    df_chart2,
    x="Department",
    y="Count",
    color="Assessment_Status",
    text=df_chart2["Percent"].astype(str) + "%",
    color_discrete_map=ASSESSMENT_COLORS,
    title="Department-wise Assessment Result (%)"
)

fig2.update_traces(textposition="inside")
st.plotly_chart(fig2, use_container_width=True)

# ==================================================
# DETAIL TABLE
# ==================================================
st.subheader("Training Details")

st.dataframe(
    df_filt.sort_values(
        by=["Training_Name", "Department", "Employee"]
    ),
    use_container_width=True
)
