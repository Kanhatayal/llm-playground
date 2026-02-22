🚀 AI Engineer Playground: Phase 1
This is the first project in my journey to becoming an AI Engineer. It is a cloud-native LLM Playground that allows users to interact with state-of-the-art models and experiment with generation parameters like Temperature and Top-P.

Live Demo: [Click here to view the app](https://llm-playground-hbppyjfmg3tpqwmz7rgg83.streamlit.app/)

🛠️ Tech Stack
Frontend: Streamlit

Model Orchestration: Groq API

Models: Llama 3.1, Mixtral 8x7b, Gemma 2

Deployment: Streamlit Community Cloud

Environment: GitHub Codespaces

🎯 Features
Model Swapping: Quickly switch between different Large Language Models.

Hyperparameter Tuning: Real-time sliders for Temperature (randomness) and Top-P (nucleus sampling).

Cloud-Native: Zero local installation required; everything runs in the cloud.

📖 What I Learned in Phase 1
Transformer Architecture: Understanding how attention mechanisms and tokenization (BPE) work.

API Integration: Connecting a web interface to high-performance inference engines (Groq).

Secrets Management: Securing API keys using Streamlit's encrypted secrets management.

CI/CD: Deploying automatically from GitHub to a live web URL.

🚀 How to Run Locally
If you want to run this project on your own machine:

Clone the repository: git clone https://github.com/kanhatayal/llm-playground.git

Install dependencies: pip install -r requirements.txt

Set up your .streamlit/secrets.toml with your GROQ_API_KEY.

Run the app: streamlit run app.py