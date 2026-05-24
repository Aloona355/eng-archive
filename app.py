import streamlit as st
import time

# ===== PAGE CONFIG =====
st.set_page_config(
    page_title="نظام أرشفة المشاريع الهندسية",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===== FAKE DATA =====
PROJECTS = [
    {"id": 1, "name": "فيلا النور", "type": "فيلا سكنية", "owner": "عمر الحارثي", "city": "جدة", "stage": "مشروع نهائي", "year": "2023", "files": 3, "progress": 75},
    {"id": 2, "name": "مخطط الواجهة", "type": "تخطيط عمراني", "owner": "شركة التطوير العمراني", "city": "مكة المكرمة", "stage": "مكتمل", "year": "2022", "files": 5, "progress": 100},
    {"id": 3, "name": "أبراج السلام", "type": "تصميم معماري", "owner": "شركة البناء الحديث", "city": "مكة المكرمة", "stage": "مشروع ابتدائي", "year": "2024", "files": 2, "progress": 45},
    {"id": 4, "name": "فندق الراحة", "type": "فندق", "owner": "شركة الضيافة الذهبية", "city": "مكة المكرمة", "stage": "مكتمل", "year": "2022", "files": 12, "progress": 100},
    {"id": 5, "name": "فيلا الربيع", "type": "فيلا سكنية", "owner": "فيصل القحطاني", "city": "جدة", "stage": "مكتمل", "year": "2023", "files": 4, "progress": 100},
    {"id": 6, "name": "مجمع الأفق التجاري", "type": "إداري تجاري", "owner": "شركة الأفق للاستثمار", "city": "مكة المكرمة", "stage": "كروكي", "year": "2024", "files": 1, "progress": 20},
    {"id": 7, "name": "عمارة الفجر", "type": "عمارة سكنية", "owner": "ناصر العمري", "city": "الرياض", "stage": "مشروع نهائي", "year": "2023", "files": 6, "progress": 75},
    {"id": 8, "name": "مول الواحة", "type": "تجاري", "owner": "مجموعة التجارة المتحدة", "city": "مكة المكرمة", "stage": "مكتمل", "year": "2021", "files": 8, "progress": 100},
]

CLIENTS = [
    {"name": "عمر الحارثي", "phone": "0501234567", "projects": 2},
    {"name": "فيصل القحطاني", "phone": "0557891234", "projects": 1},
    {"name": "ناصر العمري", "phone": "0534567890", "projects": 3},
    {"name": "بندر الشمري", "phone": "0509876543", "projects": 1},
    {"name": "شركة البناء الحديث", "phone": "0126543210", "projects": 1},
]

# ===== CSS =====
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;900&display=swap');

* {
    font-family: 'Cairo', sans-serif !important;
}

html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif !important;
    direction: rtl;
    color: #ffffff !important;
}

.main {
    background: #0f1117;
}

.stApp {
    background: #0f1117;
    color: #ffffff !important;
}

/* كل النصوص */
h1, h2, h3, h4, h5, h6,
p, span, div, label,
[data-testid="stMarkdownContainer"],
[data-testid="stText"],
.stMarkdown,
.stText,
section,
small {
    color: #ffffff !important;
}

/* اخفاء عناصر Streamlit */
#MainMenu,
footer,
header {
    visibility: hidden;
}

.stDeployButton {
    display: none;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: #161b27 !important;
    border-left: 1px solid rgba(255,255,255,0.08);
}

[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

/* أزرار السايدبار */
[data-testid="stSidebar"] .stButton > button {
    background-color: #1c2333 !important;
    color: #ffffff !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
}

[data-testid="stSidebar"] .stButton > button:hover {
    background-color: #222b3d !important;
    border-color: rgba(79,142,247,0.5) !important;
}

/* الأزرار العامة */
.stButton > button {
    font-family: 'Cairo', sans-serif !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    color: #ffffff !important;
}

/* حقول الإدخال */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div {
    background: #1c2333 !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    color: #ffffff !important;
    direction: rtl !important;
}

/* النص داخل الحقول */
input,
textarea {
    color: #ffffff !important;
    caret-color: #ffffff !important;
}

/* Placeholder */
input::placeholder,
textarea::placeholder {
    color: rgba(255,255,255,0.45) !important;
}

/* Selectbox */
.stSelectbox div[data-baseweb="select"] * {
    background: #1c2333 !important;
    color: #ffffff !important;
}

/* الفورمز */
div[data-testid="stForm"] {
    background: #1c2333;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 12px;
    padding: 20px;
}

/* التابات */
.stTabs [data-baseweb="tab-list"] {
    background: #161b27;
    border-radius: 10px;
    padding: 4px;
}

.stTabs [data-baseweb="tab"] {
    color: #ffffff !important;
}

.stTabs [aria-selected="true"] {
    color: #4f8ef7 !important;
    background: #1c2333 !important;
    border-radius: 8px !important;
}

/* إخفاء النصوص المساعدة تحت الحقول */
[data-testid="InputInstructions"] {
    display: none !important;
}

small {
    display: none !important;
}

p[id*="instruction"] {
    display: none !important;
}

.stTextInput div[data-baseweb="base-input"] ~ div {
    display: none !important;
}

.stTextArea div[data-baseweb="base-input"] ~ div {
    display: none !important;
}

/* إخفاء زر فتح/إغلاق السايدبار */
[data-testid="collapsedControl"] {
    display: none !important;
}

[data-testid="stSidebarCollapseButton"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# ===========================
# LOGIN PAGE
# ===========================
def login_page():
    st.markdown("""
    <style>
    /* Login page full screen */
    .login-wrap {
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 80vh;
        direction: rtl;
    }
    .login-box {
        background: #1c2333;
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 36px 32px;
        width: 380px;
    }
    .login-title {
        font-size: 22px;
        font-weight: 800;
        color: #ffffff;
        text-align: center;
        font-family: Cairo, sans-serif;
        margin-bottom: 4px;
    }
    .login-sub {
        font-size: 13px;
        color: #6b7280;
        text-align: center;
        font-family: Cairo, sans-serif;
        margin-bottom: 28px;
    }
    .login-label {
        font-size: 13px;
        font-weight: 600;
        color: #ffffff;
        font-family: Cairo, sans-serif;
        margin-bottom: 6px;
        text-align: right;
    }
    /* Input styling - login only */
    .stTextInput > div > div > input {
        background: #0d1117 !important;
        border: 1px solid rgba(255,255,255,0.12) !important;
        border-radius: 8px !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        caret-color: #ffffff !important;
        font-family: Cairo, sans-serif !important;
        font-size: 14px !important;
    }
    .stTextInput > div > div > input::placeholder {
        color: rgba(255,255,255,0.25) !important;
        -webkit-text-fill-color: rgba(255,255,255,0.25) !important;
    }
    .stTextInput > div > div > input:-webkit-autofill {
        -webkit-box-shadow: 0 0 0px 1000px #0d1117 inset !important;
        -webkit-text-fill-color: #ffffff !important;
    }
    .stTextInput label { display: none !important; }
    /* Force sidebar dark - override any login CSS leak */
    [data-testid="stSidebar"],
    [data-testid="stSidebar"] > div,
    section[data-testid="stSidebar"] {
        background-color: #161b27 !important;
        background: #161b27 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<div class='login-title'>نظام الأرشفة الهندسية</div>", unsafe_allow_html=True)
        st.markdown("<div class='login-sub'>Engineering Archive System</div>", unsafe_allow_html=True)

        st.markdown("<div class='login-label'>البريد الإلكتروني</div>", unsafe_allow_html=True)
        email = st.text_input("e", placeholder="engineer@company.com", label_visibility="collapsed")

        st.markdown("<div class='login-label' style='margin-top:12px;'>كلمة المرور</div>", unsafe_allow_html=True)
        password = st.text_input("p", type="password", placeholder="••••••••", label_visibility="collapsed")

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("تسجيل الدخول", use_container_width=True, type="primary"):
            if (email in ["admin@eng.com", "admin"]) and password == "1234":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("بيانات خاطئة")

        st.markdown("<div style='text-align:center;color:#6b7280;font-size:12px;margin-top:12px;font-family:Cairo,sans-serif;'>تجربة: admin@eng.com / 1234</div>", unsafe_allow_html=True)

# ===========================
# SIDEBAR
# ===========================
def render_sidebar():
    st.markdown("""
    <style>
    [data-testid="stSidebar"],
    [data-testid="stSidebar"] > div,
    section[data-testid="stSidebar"],
    .css-1d391kg, .css-ffhzg2 {
        background: #161b27 !important;
        background-color: #161b27 !important;
        border-left: 1px solid rgba(255,255,255,0.08) !important;
        min-width: 220px !important;
        max-width: 220px !important;
    }

    [data-testid="stSidebar"] * {
        color: #e8eaf0 !important;
        font-family: 'Cairo', sans-serif !important;
    }

    [data-testid="collapsedControl"] {
        display: none !important;
    }

    [data-testid="stSidebarCollapseButton"] {
        display: none !important;
    }

    section[data-testid="stSidebar"] > div {
        padding-top: 20px !important;
    }

    /* أزرار الشريط الجانبي */
    [data-testid="stSidebar"] .stButton > button {
        background-color: #1c2333 !important;
        color: #e8eaf0 !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        box-shadow: none !important;
    }

    [data-testid="stSidebar"] .stButton > button:hover {
        background-color: #222b3d !important;
        color: #ffffff !important;
        border-color: rgba(79,142,247,0.5) !important;
    }

    [data-testid="stSidebar"] .stButton > button:focus,
    [data-testid="stSidebar"] .stButton > button:active {
        background-color: #1c2333 !important;
        color: #ffffff !important;
        border-color: #4f8ef7 !important;
        outline: none !important;
        box-shadow: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.markdown("""
        <div style='padding:0 0 16px; border-bottom:1px solid rgba(255,255,255,0.08); margin-bottom:16px;'>
            <div style='font-size:14px; font-weight:700; color:#e8eaf0; font-family:Cairo,sans-serif; text-align:right;'>
                نظام الأرشفة الهندسية
            </div>
        </div>
        """, unsafe_allow_html=True)

        pages = {
            "الرئيسية": "dashboard",
            "كل المشاريع": "projects",
            "شات AI": "chat",
            "مشروع جديد": "add",
            "العملاء": "clients",
            "التقارير": "reports",
        }

        for label, key in pages.items():
            if st.button(label, key=f"nav_{key}", use_container_width=True):
                st.session_state.page = key
                st.rerun()

        st.markdown("---")

        if st.button("تسجيل الخروج", key="logout", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.chat_history = []
            st.rerun()


# ===========================
# DASHBOARD
# ===========================
def page_dashboard():
    st.markdown("<div class='section-title'> نظرة عامة</div>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    metrics = [
        (c1, "24", "إجمالي المشاريع", ""),
        (c2, "8", "قيد التنفيذ", ""),
        (c3, "14", "مكتملة", ""),
        (c4, "19", "العملاء", ""),
    ]
    for col, num, label, icon in metrics:
        with col:
            st.markdown(f"""
            <div class='metric-card'>
                <div style='font-size:24px;'>{icon}</div>
                <div class='metric-num'>{num}</div>
                <div class='metric-label'>{label}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col_left, col_right = st.columns([1.2, 0.8])

    with col_left:
        st.markdown("<div class='section-title'> أحدث المشاريع</div>", unsafe_allow_html=True)
        for p in PROJECTS[:4]:
            stage_class = "stage-done" if p["stage"] == "مكتمل" else "stage-ongoing" if p["stage"] == "مشروع نهائي" else "stage-early"
            st.markdown(f"""
            <div class='project-card'>
                <div style='display:flex; justify-content:space-between; align-items:center;'>
                    <div>
                        <div style='font-size:14px; font-weight:700; color:#e8eaf0;'>{p["name"]}</div>
                        <div style='font-size:12px; color:#6b7280; margin-top:3px;'> {p["owner"]} • {p["city"]}</div>
                    </div>
                    <span class='stage-badge {stage_class}'>{p["stage"]}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with col_right:
        st.markdown("<div class='section-title'>احصائيات سريعة</div>", unsafe_allow_html=True)

        stats = [
            ("فيلا سكنية", 10, "#4f8ef7"),
            ("عمارة سكنية", 6, "#34d399"),
            ("تجاري", 4, "#fbbf24"),
            ("تخطيط عمراني", 3, "#a78bfa"),
            ("أخرى", 1, "#6b7280"),
        ]
        for label, val, color in stats:
            st.markdown(f"""
            <div style="background:#1c2333;border:1px solid rgba(255,255,255,0.08);border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;justify-content:space-between;align-items:center;">
                <span style="font-size:13px;color:#e8eaf0;">{label}</span>
                <span style="font-size:14px;font-weight:700;color:{color};">{val}</span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("افتح المساعد الذكي", use_container_width=True, type="primary"):
            st.session_state.page = "chat"
            st.rerun()

# ===========================
# ALL PROJECTS
# ===========================
def page_projects():
    st.markdown("<div class='section-title'> كل المشاريع</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        search = st.text_input(" بحث", placeholder="اسم المشروع أو العميل...")
    with col2:
        filter_type = st.selectbox("النوع", ["الكل", "فيلا سكنية", "عمارة سكنية", "تصميم معماري", "فندق", "تجاري", "تخطيط عمراني"])
    with col3:
        filter_stage = st.selectbox("المرحلة", ["الكل", "كروكي", "مشروع ابتدائي", "مشروع نهائي", "مكتمل"])

    filtered = PROJECTS
    if search:
        filtered = [p for p in filtered if search in p["name"] or search in p["owner"]]
    if filter_type != "الكل":
        filtered = [p for p in filtered if p["type"] == filter_type]
    if filter_stage != "الكل":
        filtered = [p for p in filtered if p["stage"] == filter_stage]

    st.markdown(f"<div style='color:#6b7280; font-size:13px; margin:10px 0;'>تم العثور على {len(filtered)} مشروع</div>", unsafe_allow_html=True)

    cols = st.columns(3)
    for i, p in enumerate(filtered):
        with cols[i % 3]:
            stage_class = "stage-done" if p["stage"] == "مكتمل" else "stage-ongoing" if p["stage"] == "مشروع نهائي" else "stage-early"
            st.markdown(f"""
            <div class='project-card'>
                <div style='font-size:11px; color:#4f8ef7; margin-bottom:8px;'>{p["type"]}</div>
                <div style='font-size:15px; font-weight:700; color:#e8eaf0;'>{p["name"]}</div>
                <div style='font-size:12px; color:#6b7280; margin:6px 0 10px;'> {p["owner"]} • {p["city"]}</div>
                <div style='background:rgba(255,255,255,0.06); border-radius:4px; height:4px; margin-bottom:8px;'>
                    <div style='background:#4f8ef7; height:4px; border-radius:4px; width:{p["progress"]}%;'></div>
                </div>
                <div style='display:flex; justify-content:space-between;'>
                    <span class='stage-badge {stage_class}'>{p["stage"]}</span>
                    <span style='font-size:11px; color:#6b7280;'> {p["files"]} ملفات</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(" فتح", key=f"open_{p['id']}", use_container_width=True):
                st.session_state.page = "detail"
                st.session_state.selected_project = p
                st.rerun()

# ===========================
# AI CHAT
# ===========================
def page_chat():
    st.markdown("""
    <div style='text-align:center; padding:10px 0 20px;'>
        <div style='font-size:40px;'></div>
        <div style='font-size:18px; font-weight:800; color:#e8eaf0; margin-top:8px;'>المساعد الذكي</div>
        <div style='font-size:13px; color:#6b7280; margin-top:4px;'>ابحث عن أي مشروع أو عميل بكلمة واحدة</div>
    </div>
    """, unsafe_allow_html=True)

    # Quick suggestions
    st.markdown("<div style='color:#6b7280; font-size:12px; margin-bottom:8px;'>اقتراحات:</div>", unsafe_allow_html=True)
    cols = st.columns(4)
    suggestions = ["المشاريع قيد التنفيذ", "كم مشروع في جدة؟", "المشاريع المكتملة", "تقرير 2023"]
    for i, sug in enumerate(suggestions):
        with cols[i]:
            if st.button(sug, key=f"sug_{i}", use_container_width=True):
                st.session_state.chat_history.append({"role": "user", "text": sug})
                response = get_ai_response(sug)
                st.session_state.chat_history.append({"role": "ai", "text": response})
                st.rerun()

    # Chat history
    if not st.session_state.chat_history:
        st.markdown("""
        <div class='chat-msg-ai'>
            أهلاً!  أنا مساعدك الذكي لأرشيف المشاريع.<br>
            اسألني مثلاً: <em style='color:#4f8ef7'>"المشاريع المكتملة"</em> أو <em style='color:#4f8ef7'>"كم مشروع في جدة؟"</em>
        </div>
        """, unsafe_allow_html=True)
    else:
        for msg in st.session_state.chat_history:
            if msg["role"] == "user":
                st.markdown(f"<div class='chat-msg-user'> {msg['text']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='chat-msg-ai'> {msg['text']}</div>", unsafe_allow_html=True)

    # Input
    st.markdown("<br>", unsafe_allow_html=True)
    with st.form("chat_form", clear_on_submit=True):
        col1, col2 = st.columns([5, 1])
        with col1:
            user_input = st.text_input("", placeholder="اكتب سؤالك... مثال: وين مشروع الغامدي؟", label_visibility="collapsed")
        with col2:
            send = st.form_submit_button("إرسال ↑", use_container_width=True, type="primary")

        if send and user_input:
            st.session_state.chat_history.append({"role": "user", "text": user_input})
            with st.spinner("جاري البحث..."):
                time.sleep(0.8)
            response = get_ai_response(user_input)
            st.session_state.chat_history.append({"role": "ai", "text": response})
            st.rerun()

    if st.button(" مسح المحادثة", key="clear_chat"):
        st.session_state.chat_history = []
        st.rerun()

def get_ai_response(text):
    text_lower = text.lower()

    # Search by project name / owner
    for p in PROJECTS:
        if any(word in text for word in p["name"].split() + p["owner"].split()):
            stage_emoji = "" if p["stage"] == "مكتمل" else ""
            return f"""وجدت المشروع! <br><br>
             <strong>{p['name']}</strong><br>
             {p['owner']}<br>
             {p['city']} •  {p['year']}<br>
            {stage_emoji} {p['stage']} •  {p['files']} ملفات<br><br>
            <em style='color:#4f8ef7;'>اضغط على "كل المشاريع" لفتح الملف كامل</em>"""

    if any(w in text for w in ["جدة", "مكة", "الرياض"]):
        city = "جدة" if "جدة" in text else "مكة المكرمة" if "مكة" in text else "الرياض"
        count = len([p for p in PROJECTS if p["city"] == city])
        names = "، ".join([p["name"] for p in PROJECTS if p["city"] == city])
        return f"عندكم <strong style='color:#4f8ef7;'>{count} مشاريع</strong> في {city} <br><br>وهي: {names}"

    if any(w in text for w in ["مكتمل", "منته", "منجز"]):
        done = [p for p in PROJECTS if p["stage"] == "مكتمل"]
        names = "، ".join([p["name"] for p in done])
        return f"عندكم <strong style='color:#34d399;'>{len(done)} مشاريع مكتملة</strong> <br><br>{names}"

    if any(w in text for w in ["تقرير", "إحصاء", "2023", "2024"]):
        year = "2023" if "2023" in text else "2024"
        count = len([p for p in PROJECTS if p["year"] == year])
        return f" تقرير {year}:<br>• عدد المشاريع: <strong style='color:#4f8ef7;'>{count}</strong><br>• المكتملة: {len([p for p in PROJECTS if p['year'] == year and p['stage'] == 'مكتمل'])}<br>• قيد التنفيذ: {len([p for p in PROJECTS if p['year'] == year and p['stage'] != 'مكتمل'])}"

    if any(w in text for w in ["كم", "عدد", "إجمالي"]):
        return f"إجمالي المشاريع: <strong style='color:#4f8ef7;'>24 مشروع</strong> <br>• قيد التنفيذ: 8<br>• مكتملة: 14<br>• كروكي فقط: 2"

    return f"بحثت في الأرشيف ولم أجد نتيجة دقيقة لـ '<em>{text}</em>' <br>جرب: اسم العميل، المدينة، أو نوع المشروع."

# ===========================
# ADD PROJECT
# ===========================
def page_add():
    st.markdown("<div class='section-title'> إضافة مشروع جديد</div>", unsafe_allow_html=True)

    with st.form("add_project"):
        st.markdown("** بيانات المشروع**")
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("اسم المشروع *", placeholder="اسم المشروع")
            p_type = st.selectbox("نوع المشروع *", ["اختر النوع", "فيلا سكنية", "عمارة سكنية", "مبنى تجاري", "فندق", "تخطيط عمراني", "تصميم داخلي"])
        with col2:
            stage = st.selectbox("مرحلة المشروع", ["اختر المرحلة", "كروكي", "مشروع ابتدائي", "مشروع نهائي", "قيد التنفيذ", "مكتمل"])
            city = st.selectbox("المدينة", ["اختر المدينة", "مكة المكرمة", "جدة", "الرياض", "المدينة المنورة"])

        st.markdown("** بيانات العميل**")
        col3, col4 = st.columns(2)
        with col3:
            owner = st.text_input("اسم العميل *", placeholder="الاسم الكامل")
            phone = st.text_input("رقم الجوال", placeholder="05XXXXXXXX")
        with col4:
            id_num = st.text_input("رقم الهوية", placeholder="1XXXXXXXXX")
            email = st.text_input("البريد الإلكتروني", placeholder="client@email.com")

        st.markdown("** رفع الملفات**")
        col5, col6, col7 = st.columns(3)
        with col5:
            sketch = st.file_uploader(" الكروكي", type=["png", "jpg", "pdf"])
        with col6:
            initial = st.file_uploader(" المشروع الابتدائي", type=["pdf", "dwg"])
        with col7:
            final = st.file_uploader(" المشروع النهائي", type=["pdf", "dwg"])

        submitted = st.form_submit_button(" حفظ المشروع", use_container_width=True, type="primary")
        if submitted:
            if name and owner:
                st.success(f" تم حفظ مشروع '{name}' بنجاح!")
                st.balloons()
            else:
                st.error(" الرجاء إدخال اسم المشروع والعميل")

# ===========================
# PROJECT DETAIL
# ===========================
def page_detail():
    p = st.session_state.get("selected_project", PROJECTS[0])

    col_title, col_btn = st.columns([3, 1])
    with col_title:
        st.markdown(f"""
        <div style='direction:rtl;'>
            <div style='font-size:11px; color:#4f8ef7; margin-bottom:6px;'>{p["type"]}</div>
            <div style='font-size:24px; font-weight:900; color:#e8eaf0;'>{p["name"]}</div>
            <div style='font-size:13px; color:#6b7280; margin-top:4px;'> {p["city"]}، المملكة العربية السعودية</div>
        </div>
        """, unsafe_allow_html=True)
    with col_btn:
        st.button(" إرسال للعميل", type="primary", use_container_width=True)
        st.button(" تعديل", use_container_width=True)

    # Info grid
    c1, c2, c3, c4 = st.columns(4)
    infos = [
        (c1, "صاحب المشروع", p["owner"]),
        (c2, "المدينة", p["city"]),
        (c3, "السنة", p["year"]),
        (c4, "الحالة", p["stage"]),
    ]
    for col, label, val in infos:
        with col:
            st.markdown(f"""
            <div style='background:#1c2333; border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:14px; text-align:center;'>
                <div style='font-size:11px; color:#6b7280;'>{label}</div>
                <div style='font-size:14px; font-weight:700; color:#e8eaf0; margin-top:4px;'>{val}</div>
            </div>
            """, unsafe_allow_html=True)

    # Timeline
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'> مراحل المشروع</div>", unsafe_allow_html=True)

    stages = ["استلام الطلب", "الكروكي", "ابتدائي", "نهائي", "تسليم"]
    stage_map = {"كروكي": 1, "مشروع ابتدائي": 2, "مشروع نهائي": 3, "مكتمل": 4}
    current = stage_map.get(p["stage"], 2)

    cols = st.columns(5)
    for i, (col, s) in enumerate(zip(cols, stages)):
        with col:
            if i < current:
                st.markdown(f"<div style='text-align:center;'><div style='width:36px;height:36px;background:rgba(79,142,247,0.15);border:2px solid #4f8ef7;border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto;color:#4f8ef7;font-weight:700;'></div><div style='font-size:11px;color:#6b7280;margin-top:6px;'>{s}</div></div>", unsafe_allow_html=True)
            elif i == current:
                st.markdown(f"<div style='text-align:center;'><div style='width:36px;height:36px;background:rgba(251,191,36,0.15);border:2px solid #fbbf24;border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto;color:#fbbf24;font-weight:700;'></div><div style='font-size:11px;color:#fbbf24;margin-top:6px;'>{s}</div></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='text-align:center;'><div style='width:36px;height:36px;border:2px solid rgba(255,255,255,0.1);border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto;color:#6b7280;'></div><div style='font-size:11px;color:#6b7280;margin-top:6px;'>{s}</div></div>", unsafe_allow_html=True)

    # Files
    st.markdown("<br>", unsafe_allow_html=True)
    col_files, col_add = st.columns([4, 1])
    with col_files:
        st.markdown("<div class='section-title'> ملفات المشروع</div>", unsafe_allow_html=True)
    with col_add:
        st.button(" إضافة ملف", use_container_width=True)

    fc1, fc2, fc3 = st.columns(3)
    files = [
        (fc1, "", "الكروكي الأصلي", "JPG • 2.4 MB"),
        (fc2, "", "المشروع الابتدائي", "PDF • 8.1 MB"),
        (fc3, "", "المشروع النهائي", "PDF • 12.3 MB"),
    ]
    for col, icon, fname, fsize in files:
        with col:
            st.markdown(f"""
            <div class='file-card'>
                <div style='font-size:32px; margin-bottom:8px;'>{icon}</div>
                <div style='font-size:13px; font-weight:700; color:#e8eaf0;'>{fname}</div>
                <div style='font-size:11px; color:#6b7280; margin:4px 0 10px;'>{fsize}</div>
            </div>
            """, unsafe_allow_html=True)
            st.button(f" عرض", key=f"view_{fname}", use_container_width=True)

# ===========================
# CLIENTS
# ===========================
def page_clients():
    st.markdown("<div class='section-title'>العملاء</div>", unsafe_allow_html=True)

    search_client = st.text_input("بحث باسم العميل", placeholder="اكتب اسم العميل...")

    filtered_clients = CLIENTS
    if search_client:
        filtered_clients = [c for c in CLIENTS if search_client in c["name"]]

    for c in filtered_clients:
        col1, col2, col3 = st.columns([0.5, 3, 1])
        with col1:
            first_letter = c['name'][0] if c['name'] else "؟"
            st.markdown(f"<div style='width:42px;height:42px;background:linear-gradient(135deg,#4f8ef7,#7fb3ff);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:18px;font-weight:700;color:white;font-family:Cairo,sans-serif;'>{first_letter}</div>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<div style='color:#e8eaf0;font-weight:700;font-family:Cairo,sans-serif;'>{c['name']}</div><div style='color:#6b7280;font-size:12px;font-family:Cairo,sans-serif;'>{c['phone']} • {c['projects']} مشاريع</div>", unsafe_allow_html=True)
        with col3:
            if st.button("عرض المشاريع", key=f"client_{c['name']}", use_container_width=True):
                st.session_state.selected_client = c["name"]
                st.session_state.page = "client_projects"
                st.rerun()
        st.markdown("<hr style='border-color:rgba(255,255,255,0.06);'>", unsafe_allow_html=True)

    if search_client and not filtered_clients:
        st.info("لم يتم العثور على عميل بهذا الاسم")

# ===========================
# CLIENT PROJECTS
# ===========================
def page_client_projects():
    client_name = st.session_state.get("selected_client", "")
    st.markdown(f"<div class='section-title'>مشاريع {client_name}</div>", unsafe_allow_html=True)

    if st.button("رجوع للعملاء", use_container_width=False):
        st.session_state.page = "clients"
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    client_projects = [p for p in PROJECTS if p["owner"] == client_name]

    if not client_projects:
        st.info("لا توجد مشاريع لهذا العميل في الأرشيف")
        return

    cols = st.columns(3)
    for i, p in enumerate(client_projects):
        with cols[i % 3]:
            stage_class = "stage-done" if p["stage"] == "مكتمل" else "stage-ongoing" if p["stage"] == "مشروع نهائي" else "stage-early"
            st.markdown(f"""
            <div class='project-card'>
                <div style='font-size:11px; color:#4f8ef7; margin-bottom:8px;'>{p["type"]}</div>
                <div style='font-size:15px; font-weight:700; color:#e8eaf0;'>{p["name"]}</div>
                <div style='font-size:12px; color:#6b7280; margin:6px 0 10px;'>{p["city"]} • {p["year"]}</div>
                <div style='background:rgba(255,255,255,0.06); border-radius:4px; height:4px; margin-bottom:8px;'>
                    <div style='background:#4f8ef7; height:4px; border-radius:4px; width:{p["progress"]}%;'></div>
                </div>
                <span class='stage-badge {stage_class}'>{p["stage"]}</span>
            </div>
            """, unsafe_allow_html=True)
            if st.button("فتح المشروع", key=f"cp_{p['id']}", use_container_width=True):
                st.session_state.selected_project = p
                st.session_state.page = "detail"
                st.rerun()

# ===========================
# REPORTS
# ===========================
def page_reports():
    st.markdown("<div class='section-title'> التقارير</div>", unsafe_allow_html=True)
    reports = [
        ("", "تقرير المشاريع الشهري", "ملخص كامل لكل مشاريع الشهر الحالي"),
        ("", "تقرير العملاء", "قائمة العملاء ومشاريعهم ومراحلها"),
        ("", "إحصائيات سنوية", "تحليل المشاريع والإنجازات خلال السنة"),
    ]
    cols = st.columns(3)
    for col, (icon, name, desc) in zip(cols, reports):
        with col:
            st.markdown(f"""
            <div style='background:#1c2333;border:1px solid rgba(255,255,255,0.08);border-radius:14px;padding:24px;text-align:center;'>
                <div style='font-size:36px;margin-bottom:12px;'>{icon}</div>
                <div style='font-size:14px;font-weight:700;color:#e8eaf0;margin-bottom:8px;'>{name}</div>
                <div style='font-size:12px;color:#6b7280;line-height:1.6;'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f" توليد PDF", key=f"report_{name}", use_container_width=True, type="primary"):
                st.success(f" جاري توليد {name}...")

# ===========================
# MAIN ROUTER
# ===========================
if not st.session_state.logged_in:
    login_page()
else:
    render_sidebar()
    page = st.session_state.page

    page_map = {
        "dashboard":       (page_dashboard,       "لوحة التحكم"),
        "projects":        (page_projects,         "كل المشاريع"),
        "chat":            (page_chat,             "المساعد الذكي"),
        "add":             (page_add,              "مشروع جديد"),
        "detail":          (page_detail,           "تفاصيل المشروع"),
        "clients":         (page_clients,          "العملاء"),
        "client_projects": (page_client_projects,  "مشاريع العميل"),
        "reports":         (page_reports,          "التقارير"),
    }

    func, title = page_map.get(page, (page_dashboard, " لوحة التحكم"))
    func()
