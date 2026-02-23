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

import streamlit as st
import pandas as pd

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="Reports | SSI Learning & Development",
    layout="wide"
)

# ==================================================
# GLOBAL STYLES (MATCH HOME THEME)
# ==================================================
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F0F2F6;
    }

    /* Page Title */
    .page-title {
        font-size: 34px;
        font-weight: 800;
        color: #0B3C5D;
        margin-bottom: 10px;
    }

    .page-subtitle {
        color: #555;
        margin-bottom: 30px;
        font-size: 16px;
    }

    /* Report cards */
    .report-card {
        background: white;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 8px 22px rgba(0,0,0,0.08);
        height: 260px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: all 0.3s ease;
    }

    .report-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 14px 30px rgba(0,0,0,0.14);
    }

    .report-card h3 {
        color: #0B3C5D;
        margin-bottom: 10px;
    }

    .report-card p {
        color: #555;
        font-size: 14px;
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
# ==================================================
# PAGE HEADER
# ==================================================
st.markdown(
    """
    <div class="page-title">📄 Reports</div>
    <div class="page-subtitle">
        Download structured training reports, summaries, and audit-ready exports.
    </div>
    """,
    unsafe_allow_html=True
)

# ==================================================
# LOAD DATA (OPTIONAL – SAFE)
# ==================================================
FILE = "training_data.xlsx"

@st.cache_data
def load_data():
    try:
        return pd.read_excel(FILE)
    except Exception:
        return pd.DataFrame()

df = load_data()

# ==================================================
# REPORT CARDS
# ==================================================
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="report-card">
        <div>
            <h3>📊 Training Summary</h3>
            <p>
                Overall training completion, participation,
                and department-wise statistics.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.download_button(
        "Download Summary (Excel)",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="training_summary.csv",
        mime="text/csv"
    )

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="report-card">
        <div>
            <h3>📝 Assessment Report</h3>
            <p>
                Pass / Fail breakdown, assessment outcomes,
                and evaluation metrics.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.download_button(
        "Download Assessment Report",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="assessment_report.csv",
        mime="text/csv"
    )

    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="report-card">
        <div>
            <h3>🏢 Department-wise Report</h3>
            <p>
                Department-level training coverage,
                pending trainings, and completion status.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.download_button(
        "Download Department Report",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="department_report.csv",
        mime="text/csv"
    )

    st.markdown("</div>", unsafe_allow_html=True)

# ==================================================
# FOOTER
# ==================================================
st.markdown(
    """
    <hr style="margin-top:60px;">
    <p style="text-align:center; color:#888;">
    © 2026 SS Innovations International, Inc. | Internal Use Only
    </p>
    """,
    unsafe_allow_html=True
)
