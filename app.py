import streamlit as st
from groq_llm_chain import generate_email

# Page config with emoji and layout
st.set_page_config(
    page_title="AI Email Composer",
    page_icon="📧",
    layout="centered",
)

# Custom background and style using HTML
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f4f7;
    }
    .block-container {
        padding-top: 2rem;
    }
    h1 {
        color: #3E64FF;
        text-align: center;
        font-size: 3em;
        margin-bottom: 0.5em;
    }
    .stTextInput > label, .stTextArea > label, .stSelectbox > label {
        font-weight: bold;
        color: #333;
    }
    .stButton > button {
        background-color: #3E64FF;
        color: white;
        font-weight: bold;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown("<h1>📧 Smart AI Email Generator</h1>", unsafe_allow_html=True)
st.markdown("✨ Generate professional & polished emails in seconds — powered by Generative AI!", unsafe_allow_html=True)
st.markdown("---")

# Input fields
purpose = st.text_input("📝 What is the purpose of your email?")
tone = st.selectbox("🎯 Select the tone", ["Formal", "Friendly", "Persuasive", "Apologetic", "Thankful"])
details = st.text_area("📌 Add any key points or context")

# Generate email
if st.button("🚀 Generate Email"):
    if not purpose or not details:
        st.warning("⚠️ Please fill out both the purpose and the details.")
    else:
        with st.spinner("🧠 Thinking... Generating your email..."):
            email = generate_email(purpose, tone, details)
            st.success("✅ Email Generated!")
            st.markdown("#### ✉️ Here’s your email:")
            st.code(email, language='markdown')
