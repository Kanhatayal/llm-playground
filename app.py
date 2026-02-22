import streamlit as st
from groq import Groq

# 1. Setup the UI Page
st.set_page_config(page_title="AI Engineer Playground", layout="centered")
st.title("🚀 LLM Playground: Phase 1")
st.subheader("Experiment with Temperature & Models")

# 2. Sidebar for Controls
st.sidebar.header("Model Configuration")
model_option = st.sidebar.selectbox(
    "Choose a Model",
    ("llama3-8b-8192", "mixtral-8x7b-32768", "gemma-7b-it")
)

temp = st.sidebar.slider("Temperature (Randomness)", 0.0, 2.0, 0.7)
top_p = st.sidebar.slider("Top-P (Nucleus Sampling)", 0.0, 1.0, 1.0)

# 3. Initialize Groq Client using Streamlit Secrets
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# 4. Chat Interface
user_input = st.text_area("Enter your prompt:", placeholder="Ask me anything...")

if st.button("Generate Response"):
    if user_input:
        with st.spinner("Model is thinking..."):
            try:
                chat_completion = client.chat.completions.create(
                    messages=[{"role": "user", "content": user_input}],
                    model=model_option,
                    temperature=temp,
                    top_p=top_p,
                )
                st.markdown("### Response:")
                st.write(chat_completion.choices[0].message.content)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a prompt first!")