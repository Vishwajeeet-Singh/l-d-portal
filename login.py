import streamlit as st
import pandas as pd

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="Login | SSI Learning & Development Portal",
    layout="wide"
)

# ==================================================
# SESSION INIT
# ==================================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = None
if "user_role" not in st.session_state:
    st.session_state.user_role = None

# ==================================================
# LOAD USERS (FROM users.xlsx)
# ==================================================
@st.cache_data
def load_users():
    df = pd.read_excel("users.xlsx")

    df["email"] = df["email"].astype(str).str.strip().str.lower()
    df["password"] = df["password"].astype(str).str.strip()
    df["role"] = df["role"].astype(str).str.strip().str.lower()

    return df

users_df = load_users()

# ==================================================
# GLOBAL THEME
# ==================================================
st.markdown("""
<style>
.stApp {
    background-color: #ADD8E6;
}

[data-testid="stHeader"] {
    background: linear-gradient(180deg, #0B3C5D, #06283D);
}
[data-testid="stHeader"] * {
    color: white !important;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0B3C5D, #07263D);
}

.login-card {
    background: white;
    padding: 45px;
    border-radius: 20px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.25);
    max-width: 420px;
    margin: 80px auto;
}

.login-title {
    text-align: center;
    font-size: 30px;
    font-weight: 800;
    color: #0B3C5D;
    margin-bottom: 25px;
}

.login-subtitle {
    text-align: center;
    color: #555;
    margin-bottom: 25px;
}

.stButton button {
    background-color: #1F77B4;
    color: white;
    font-weight: 600;
    border-radius: 10px;
    width: 100%;
    padding: 12px;
}

.stButton button:hover {
    background-color: #155A8A;
}
/* ---------------- FOOTER ---------------- */
.footer {
    text-align: center;
    color: #777;
    font-size: 13px;
    margin-top: 60px;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# HEADER BANNER
# ==================================================
st.markdown("""
<div style="
    background:
        linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)),
        url('https://ssinnovations.com/wp-content/uploads/2025/07/SSI-M3-Home-Splash-MAR25-v3.webp');
    background-size: cover;
    background-position: center;
    border-radius: 22px;
    padding: 60px 40px;
    color: white;
    text-align: center;
    margin-bottom: 40px;
">
    <h1>SSI Learning & Development Portal</h1>
    <p>Secure access to training dashboards, reports and resources</p>
</div>
""", unsafe_allow_html=True)

# ==================================================
# LOGIN FORM
# ==================================================
st.markdown("""
<div class="login-card">
    <div class="login-title">🔐 Login</div>
    <div class="login-subtitle">Use your SSI credentials</div>
</div>
""", unsafe_allow_html=True)

email = st.text_input("Email")
password = st.text_input("Password", type="password")

# ==================================================
# LOGIN LOGIC
# ==================================================
if st.button("Login"):

    email = email.strip().lower()
    password = password.strip()

    match = users_df[
        (users_df["email"] == email) &
        (users_df["password"] == password)
    ]

    if not match.empty:
        role = match.iloc[0]["role"]

        st.session_state.logged_in = True
        st.session_state.user_email = email
        st.session_state.user_role = role

        st.success("Login successful")

        # ROLE BASED REDIRECT
        if role == "admin":
            st.switch_page("pages/0_Home.py")
        else:
            st.switch_page("pages/3_Resources.py")

    else:
        st.error("Invalid email or password")
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
        Contact: Vishwajeet Singh (vishwajeet.singh@ssinnovations.org (+91 80020-60789)) <br>
                 Abhijeet Sharma (abhijeet.sharma@ssinnovations.org (+91 96508-14325))
    </div>
    """,
    unsafe_allow_html=True
)
