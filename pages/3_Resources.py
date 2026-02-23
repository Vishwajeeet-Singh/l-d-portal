import streamlit as st

# ---------------- LOGIN CHECK ----------------
if "logged_in" not in st.session_state or not st.session_state.logged_in:
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
    page_title="Learning Resources",
    layout="wide"
)

# ==================================================
# GLOBAL THEME (MATCH HOME & DASHBOARD)
# ==================================================
st.markdown("""
<style>
/* ---------- APP BACKGROUND ---------- */
.stApp {
    background-color: #ADD8E6;
}

/* ---------- TOP HEADER ---------- */
[data-testid="stHeader"] {
    background: linear-gradient(180deg, #0B3C5D, #06283D);
}

[data-testid="stHeader"] * {
    color: white !important;
}

/* ---------- SIDEBAR ---------- */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0B3C5D, #07263D);
}

[data-testid="stSidebar"] * {
    color: white !important;
    font-weight: 500;
}

/* ---------- PAGE TITLE ---------- */
.page-title {
    text-align: center;
    font-size: 36px;
    font-weight: 800;
    color: #0B3C5D;
    margin-bottom: 5px;
}

.page-subtitle {
    text-align: center;
    color: #555;
    margin-bottom: 30px;
}

/* ---------- SECTION HEADINGS ---------- */
.section-heading {
    font-size: 24px;
    font-weight: 700;
    color: #0B3C5D;
    margin: 30px 0 20px 0;
}

/* ---------- RESOURCE CARDS ---------- */
.resource-card {
    background: white;
    padding: 24px;
    border-radius: 16px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.10);
    height: 230px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: all 0.3s ease;
    border-top: 5px solid #1F77B4;
}

.resource-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 14px 30px rgba(0,0,0,0.18);
}

.resource-card h4 {
    margin-bottom: 10px;
    color: #0B3C5D;
    font-weight: 700;
}

.resource-card p {
    font-size: 14px;
    color: #555;
    line-height: 1.5;
}

/* ---------- BUTTONS ---------- */
.stButton button,
a[data-testid="stLinkButton"] {
    background-color: #1F77B4 !important;
    color: white !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    border: none !important;
}

.stButton button:hover,
a[data-testid="stLinkButton"]:hover {
    background-color: #155A8A !important;
}

/* ---------- FOOTER ---------- */
.footer {
    text-align: center;
    color: #666;
    font-size: 13px;
    margin-top: 60px;
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# PAGE TITLE
# ==================================================
st.markdown("<div class='page-title'>📚 Learning Resources</div>", unsafe_allow_html=True)
st.markdown("<div class='page-subtitle'>Access training PPTs and assessment links</div>", unsafe_allow_html=True)
st.divider()

# ==================================================
# TRAINING PPTs
# ==================================================
st.markdown("<div class='section-heading'>📊 Training PPTs</div>", unsafe_allow_html=True)

ppt_resources = [
    ("🧹 5S Methodology", "Workplace organization and efficiency principles",
     "https://ssipvtltd-my.sharepoint.com/:p:/g/personal/vishwajeet_singh_ssinnovations_org/IQAK5IpAWwyYRbGYbTTO2oqxAXmkDHPQM-HPB4XUdhJI2v4"),
    ("🔁 Kaizen", "Continuous improvement philosophy",
     "https://ssipvtltd-my.sharepoint.com/:p:/g/personal/vishwajeet_singh_ssinnovations_org/IQB4TcNaDb1XSpsGkmSsnBx2AfA5r3krFKRHde56ojjgZOM"),
    ("🛑 Poka-Yoke", "Mistake-proofing techniques",
     "https://ssipvtltd-my.sharepoint.com/:p:/g/personal/vishwajeet_singh_ssinnovations_org/IQAEfOm-AforTJ0RXXBVXdnhAQ82egGqEJ03N8g8ZEIgpzg"),
    ("⚡ ESD", "Electro Static Discharge awareness",
     "https://ssipvtltd-my.sharepoint.com/:p:/g/personal/vishwajeet_singh_ssinnovations_org/IQB7xMmpVAzBSIleczV7sClyARsGUFdkk41QGNPJVydZn7w"),
    ("⚙️ TPM", "Total Productive Maintenance",
     "https://ssipvtltd-my.sharepoint.com/:p:/g/personal/vishwajeet_singh_ssinnovations_org/IQBPH0jYStkiSrGzNMy9n59_ASZdXUQCoaJ48sDiPJvWOKg"),
    ("🦺 OSHA Safety", "Workplace safety & compliance",
     "https://ssipvtltd-my.sharepoint.com/:p:/g/personal/vishwajeet_singh_ssinnovations_org/IQBausu3D0AURr4l69LvL60DARu_5NSGQG1oPmD0Pu9ZPR8"),
    ("📋 QMS", "Quality Management System",
     "https://ssipvtltd-my.sharepoint.com/:p:/g/personal/abhijeet_sharma_ssinnovations_org/IQBby9LKB_sCSZJ36AjHnK8NAUolaXWtC8Ty3s7AQWIUW0E"),
    ("📊 7 QC Tools", "Quality control & problem solving",
     "https://ssipvtltd-my.sharepoint.com/:p:/g/personal/vishwajeet_singh_ssinnovations_org/IQBTE2k9_MqVTqnSVOhxXyNnAQq8ItRIiBrzdByt_GDhJx4"),
    ("📦 Material Handling", "Move, Store, Protect, and Control materials safely and efficiently",
     "https://ssipvtltd-my.sharepoint.com/:p:/g/personal/vishwajeet_singh_ssinnovations_org/IQDx7LkkIp0-QZ2RwIJ1iNpJAQTLGIlColK1kXSvJnNG8DQ?e=Pgufb7"),
]
cols = st.columns(4)
for i, (title, desc, link) in enumerate(ppt_resources):
    with cols[i % 4]:
        st.markdown(f"""
        <div class="resource-card">
            <div>
                <h4>{title}</h4>
                <p>{desc}</p>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("Open PPT", link)
        st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ==================================================
# TRAINING ASSESSMENTS
# ==================================================
st.markdown("<div class='section-heading'>📝 Training Assessments</div>", unsafe_allow_html=True)

assessment_resources = [
    ("🧹 5S Assessment", "Knowledge check for 5S",
     "https://www.classmarker.com/online-test/start/?quiz=r9y68e7397bc9efe"),
    ("🔁 Kaizen Assessment", "Continuous improvement evaluation",
     "https://www.classmarker.com/online-test/start/?quiz=jp768e9e77cd684c"),
    ("🛑 Poka-Yoke Assessment", "Mistake-proofing test",
     "https://www.classmarker.com/online-test/start/?quiz=hbq68e9e81449e29"),
    ("⚡ ESD Assessment", "ESD awareness test",
     "https://www.classmarker.com/online-test/start/?quiz=qtb68e739f34535a"),
    ("⚙️ TPM Assessment", "TPM evaluation",
     "https://www.classmarker.com/online-test/start/?quiz=gjq68fc4a1ca1151"),
    ("🦺 OSHA Assessment", "Safety compliance test",
     "https://www.classmarker.com/online-test/start/?quiz=n3k68e74e66df9dc"),
    ("📋 QMS Assessment", "QMS knowledge test",
     "https://www.classmarker.com/online-test/start/?quiz=kmp690ddbae4af1a"),
    ("📊 7 QC Tools Assessment", "QC tools understanding",
     "https://www.classmarker.com/online-test/start/?quiz=kbx695baa18c2df5"),
    ("📦 Material Handling", "Move, Store, Protect, and Control materials safely and efficiently",
     "https://www.classmarker.com/online-test/start/?quiz=tnv6978978c8d7b2"),
]

cols = st.columns(4)
for i, (title, desc, link) in enumerate(assessment_resources):
    with cols[i % 4]:
        st.markdown(f"""
        <div class="resource-card">
            <div>
                <h4>{title}</h4>
                <p>{desc}</p>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("Open Assessment", link)
        st.markdown("</div>", unsafe_allow_html=True)

# ==================================================
# FOOTER
# ==================================================
st.markdown("""
<div class="footer">
    For any access issues, contact the L&D team.<br>
    © 2026 SS Innovations | Internal Use Only
</div>
""", unsafe_allow_html=True)
