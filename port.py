import streamlit as st
from streamlit_lottie import st_lottie
import requests
import google.generativeai as genai
import random

# --- Page Config ---
st.set_page_config(page_title="Sahil Desai | Portfolio", layout="wide", page_icon="💼")
# --- Apply Theme CSS ---

# --- Theme Toggle ---
if "theme" not in st.session_state:
    st.session_state["theme"] = "light"

theme_toggle = st.toggle("🌙(Dark Mode)", value=(st.session_state["theme"] == "dark"))
st.session_state["theme"] = "dark" if theme_toggle else "light"

# --- Apply Theme CSS ---
def apply_theme(theme):
    if theme == "dark":
        st.markdown("""
            <style>
                body, .stApp { background-color: #1e1e1e; color: #ffffff; }
                .css-18e3th9, .css-1d391kg { background-color: #262730; }
                h1, h2, h3, h4, h5, h6, p, li, ul { color: #ffffff !important; }
            </style>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
                body, .stApp { background-color: #ffffff; color: #000000; }
                h1, h2, h3, h4, h5, h6, p, li, ul { color: #000000 !important; }
            </style>
            """, unsafe_allow_html=True)

apply_theme(st.session_state["theme"])

st.markdown("""
    <style>
    .fade-section {
        opacity: 0;
        transform: translateY(20px);
        animation: fadeInUp 1s ease-out forwards;
    }

    @keyframes fadeInUp {
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    </style>
""", unsafe_allow_html=True)


# --- Gemini API Key (Do Not Edit This Block) ---
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Gemini API Key error: {e}")
    model = None

# --- Lottie Animation Loader ---
def load_lottie_url(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except:
        return None
    return None

# --- Lottie Animations ---
lottie_hero = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_touohxv0.json")  # Rocket launch
lottie_about = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_4kx2q32n.json")
lottie_projects = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_x1gjdldd.json")  # Projects
lottie_chatbot = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_0yfsb3a1.json")  # Chatbot
lottie_footer = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_3rwasyjy.json")   # Thank you

# --- Hero Section ---
st.markdown("""
<style>
/* HERO: container */
.intro-wrapper{
  display:flex;
  gap:32px;
  align-items:center;
  justify-content:space-between;
  margin-top:28px;
  width:100%;
}

/* TEXT */
.intro-text{
  flex:1;
  color:var(--text-color, #e6eefc);
  font-family: 'Poppins', sans-serif;
  padding: 10px 20px;
}

.intro-text h1{
  font-size:2.6rem;
  margin:0 0 8px 0;
  font-weight:800;
  letter-spacing:0.6px;
  line-height:1.02;
}

/* gradient name */
.intro-text h1 span{
  background: linear-gradient(90deg,#6a11cb 0%, #2575fc 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  display:inline-block;
  padding:2px 6px;
  transform: translateZ(0);
}

/* subtitle */
.intro-text h3{
  margin:0 0 18px 0;
  color: rgba(230,230,230,0.85);
  font-weight:600;
}

/* paragraph styling */
.intro-text p{
  margin:8px 0;
  color: rgba(230,230,230,0.82);
  font-size:1rem;
  line-height:1.55;
}

/* highlights */
.highlight { color:#00b4d8; font-weight:700; }
.highlight-red { color:#ff4d6d; font-weight:700; }

/* animation / placeholder block (replace with Lottie or image if needed) */
.intro-animation{
  width:320px;
  height:220px;
  border-radius:16px;
  background: linear-gradient(135deg, rgba(255,255,255,0.05), rgba(255,255,255,0.02));
  box-shadow: 0 8px 30px rgba(0,0,0,0.25);
  display:flex;
  align-items:center;
  justify-content:center;
  color:rgba(255,255,255,0.5);
  font-weight:700;
  font-size:0.95rem;
  backdrop-filter: blur(6px);
}

/* small responsive adjustments */
@media (max-width: 900px){
  .intro-wrapper{flex-direction:column; gap:18px}
  .intro-animation{width:100%; height:180px}
  .intro-text h1{font-size:2rem}
}
</style>

<div class="intro-wrapper">
  <div class="intro-text">
    <h1>Hey, I'm <span>Sahil Desai 👋</span></h1>
    <h3>2nd Year BTech EXTC | VJTI Mumbai</h3>

    <p>🚀 I build full-stack projects that fuse <span class="highlight">Embedded Systems</span>, <span class="highlight-red">AI</span>, and <span class="highlight">Machine Learning</span>.</p>

    <p>💻 Currently deep into <span class="highlight">Data Science</span>, training <span class="highlight-red">ML models</span>, and sharpening problem solving with <span class="highlight">DSA</span>.</p>

    <p>🧰 Working on real-world systems using <span class="highlight-red">OpenCV</span>, <span class="highlight">ESP32</span>, and <span class="highlight">Streamlit</span> — shipping ideas into working prototypes.</p>

    <p>🎯 I learn by building, so expect demos, notebooks, and neat hacks. Let’s build something wild 🚀</p>
  </div>

  <div class="intro-animation" id="hero-animation">
    Interactive Demo
  </div>
</div>
""", unsafe_allow_html=True)


if lottie_about:
    st_lottie(lottie_about, height=350, key="hero") # close fade-section div



# --- About Me ---
with st.container():
    st.markdown("<div class='fade-section'>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <style>
        .about-section h2 {
            font-family: 'Poppins', sans-serif;
            font-size: 32px;
            color: #FF4B4B;
        }
        .about-section p {
            font-family: 'Poppins', sans-serif;
            font-size: 17px;
            color: #999999;
            line-height: 1.6;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        <div class="about-section">
            <h2>🧠 About Me</h2>
            <p>I'm a tech enthusiast passionate about building real-world solutions with Embedded Systems and Python.</p>
            <p>From robotics to OpenCV to data visualizations on the web, I love to blend creativity and code.</p>
            <p>Currently learning DSA and Data Science to prepare for software internships.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        if lottie_hero:
            st_lottie(lottie_hero, height=280, key="about")
    st.markdown("</div>", unsafe_allow_html=True)

# --- Projects Section ---
with st.container():
    st.markdown("<div class='fade-section'>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <style>
        .projects-section h2 {
            font-family: 'Poppins', sans-serif;
            font-size: 32px;
            color: #FF4B4B;
            margin-bottom: 15px;
        }
        .project-box {
            font-family: 'Poppins', sans-serif;
            font-size: 17px;
            color: white;
            margin-bottom: 15px;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        .box1 { background-color: #4CAF50; }   /* Green */
        .box2 { background-color: #2196F3; }   /* Blue */
        .box3 { background-color: #FF9800; }   /* Orange */
        .box4 { background-color: #9C27B0; }   /* Purple */

        .dark .box1, .dark .box2, .dark .box3, .dark .box4 {
            filter: brightness(0.9);
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='projects-section'><h2>🛠️ Projects</h2></div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("""
        <div class='project-box box1'>🤖 <b>Self-balancing Robot</b><br>
        Built using ESP32 and MPU6050 for real-time motion balancing.</div>

        <div class='project-box box2'>🚗 <b>Wi-Fi Controlled Car</b><br>
        ESP32-based vehicle controlled via browser with live video feed.</div>

        <div class='project-box box3'>📊 <b>Smart Distance Monitoring</b><br>
        Integrated OLED + Chart.js to display distance data live on web.</div>

        <div class='project-box box4'>✋ <b>Handwriting Recognition for Kids</b><br>
        Detects alphabets using OpenCV and provides voice feedback.</div>
        """, unsafe_allow_html=True)

    with col2:
        if lottie_footer:
            st_lottie(lottie_footer, height=500, key="footer")
    st.markdown("</div>", unsafe_allow_html=True)

# --- Gemini Chatbot Section ---
with st.container():
    st.markdown("<div class='fade-section'>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <style>
        .chatbot-title {
            font-family: 'Poppins', sans-serif;
            font-size: 32px;
            color: #FF4B4B;
            margin-bottom: 0.2em;
        }
        .chat-caption {
            font-family: 'Poppins', sans-serif;
            font-size: 16px;
            color: #666;
            margin-bottom: 20px;
        }
        .chatbot-box {
            background-color: #ffffff;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.07);
            font-family: 'Poppins', sans-serif;
            color: #333;
            margin-bottom: 20px;
        }
        .chatbot-response {
            background-color: #f4f4f4;
            padding: 15px;
            margin-top: 10px;
            border-left: 5px solid #FF4B4B;
            border-radius: 10px;
            font-family: 'Poppins', sans-serif;
        }
        .dark .chatbot-box {
            background-color: #1e1e24 !important;
            color: #dddddd !important;
        }
        .dark .chatbot-response {
            background-color: #2c2f35 !important;
            color: #e0e0e0 !important;
            border-left: 5px solid #4B8BBE;
        }
        .dark .chat-caption {
            color: #aaaaaa !important;
        }
        input[type="text"] {
            font-family: 'Poppins', sans-serif;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #cccccc;
            width: 100%;
        }
        </style>

        <div class='chatbot-title'>💬 Ask Me Anything (Chatbot)</div>
        <div class='chat-caption'>Curious about Sahil’s journey, projects, or achievements? Just ask!</div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("<div class='chatbot-box'>", unsafe_allow_html=True)
        user_input = st.text_input("🔎 Type your question here:")

        if user_input and model:
            with st.spinner("🤖 Thinking..."):
                prompt = f"""
    You are an AI assistant for Sahil Desai's portfolio. Only reveal personal background info if asked directly.

    PRIVATE INFO (DO NOT reveal unless specifically asked):
    - Was a JEE dropper in 2023
    - Scored ~98 percentile in JEE Mains (2023, 2024), not qualified JEE Advanced
    - Got 99.09 percentile in MHT-CET
    - Admitted to VJTI via Defense Quota in 2024
    - 8.22 CGPA in first year
    - Allotted D-Block hostel on merit
    - Had a girlfriend in 12th (keep name private)

    User asked: {user_input}
    """
                try:
                    response = model.generate_content(prompt)
                    st.success(response.text)
                except Exception as e:
                    st.error(f"❌ AI response failed: {e}")

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        if lottie_chatbot:
            st_lottie(lottie_chatbot, height=280, key="chat")
    st.markdown("</div>", unsafe_allow_html=True)
    
# --- Footer ---
with st.container():
    st.markdown("<div class='fade-section'>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<h2>✨ Thanks for Visiting!</h2>", unsafe_allow_html=True)
    st.write("This portfolio is built with Python, Streamlit, and love for innovation.")
    if lottie_projects:
        st_lottie(lottie_projects, height=200, key="projects")
    st.markdown("</div>", unsafe_allow_html=True)




