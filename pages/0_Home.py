import streamlit as st

# ---------------- LOGIN CHECK ----------------

if not st.session_state.get("logged_in"):
    st.switch_page("login.py")

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("### 👤 Logged in user")
    st.write(st.session_state.get("user_email", ""))

    st.markdown("---")

    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.switch_page("login.py")


import streamlit as st
# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="SSI Learning & Development Portal",
    layout="wide"
)

# ==================================================
# GLOBAL THEME STYLES (BLUE CORPORATE)
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

# ==================================================
# HEADER BANNER
# ==================================================
st.markdown(
    """
    <div class="header-banner">
        <h1>SSI Learning & Development Portal</h1>
        <p>
            Track training progress, monitor assessment outcomes,
            and drive workforce capability with real-time insights.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ==================================================
# SECTION TITLE
# ==================================================
st.markdown(
    "<div class='section-title'>🚀 Choose an option</div>",
    unsafe_allow_html=True
)

# ==================================================
# NAVIGATION CARDS
# ==================================================
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="card">
            <div>
                <h3>📊 Training Dashboard</h3>
                <p>
                    View training completion, department-wise performance,
                     and assessment outcomes.
                </p>
            </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Open Dashboard"):
        st.switch_page("pages/1_Learning_Dashboard.py")

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown(
        """
        <div class="card">
            <div>
                <h3>📄 Training Reports</h3>
                <p>
                    Download structured reports, historical summaries,
                     and training data.
                </p>
            </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("View Reports"):
        st.switch_page("pages/2_Reports.py")

    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown(
        """
        <div class="card">
            <div>
                <h3>🌐 Learning Resources</h3>
                <p>
                    Access training ppts and assessement links.
                </p>
            </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Open Resources"):
        st.switch_page("pages/3_Resources.py")

    st.markdown("</div>", unsafe_allow_html=True)

# ==================================================
# FOOTER
# ==================================================
st.markdown(
    """
    <hr style="margin-top:70px;">
    <div class="footer">
        © 2026 SS Innovations International, Inc. <br>
        © 2026 Sudhir Srivastava Innovations Pvt. Ltd. <br>
        All products and product names are registered trademarks or pending trademarks. <br>
        All Rights Reserved | Internal Use Only. <br>
        Contact: Vishwajeet Singh (vishwajeet.singh@ssinnovations.org (+91 80020-60789))<br>
                 Abhijeet Sharma (abhijeet.sharma@ssinnovations.org (+91 96508-14325))
    </div>
    """,
    unsafe_allow_html=True
)
