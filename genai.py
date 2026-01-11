import google.generativeai as genai

genai.configure(api_key="AIzaSyC5qegXU7z9BfFYCqa2UFT5MSLFKwaF5-U")
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv



# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Page config
st.set_page_config(
    page_title="Gemini AI Assistant",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
    }
    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: #00d4ff;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #c7c7c7;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

# UI Header
st.markdown('<div class="title">🚀 Gemini AI Tool</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Ask anything about Cloud, DevOps, AWS & more</div>',
    unsafe_allow_html=True
)

# Input box
prompt = st.text_area(
    "💡 Enter your question",
    height=120,
    placeholder="Explain cloud computing in simple terms..."
)

# Button
if st.button("✨ Generate Answer"):
    if not prompt.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking... 🤖"):
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(prompt)
            st.success("✅ Response generated!")
            st.markdown("### 📌 AI Response")
            st.write(response.text)
