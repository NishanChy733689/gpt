# app.py
import streamlit as st
from ollama import chat

st.set_page_config(page_title="AI Chatbot with Voice & Image", layout="centered")

# -------------------- Sidebar --------------------
st.sidebar.title("🤖 AI Controls")
models = ["smollm:135m","qwen2.5-coder:1.5b","gemma3:1b","phi:latest","qwen3:0.6b","gemma3n:e2b"]
model = st.sidebar.selectbox("Choose a model", models)

if st.sidebar.button("🗑️ Clear Chat History"):
    st.session_state.messages = []
    st.rerun()
# --------------- Session State Init ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []


st.title("AI Personality Chatbot")

for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.chat_message(msg["role"]).markdown(msg["content"])

prompt = st.chat_input("Say or type something...")

# ---------------- Handle Response ----------------
if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.spinner("Thinking..."):
            response = ""   
            try:
                stream = chat(model=model, messages=st.session_state.messages, stream=True, )
            except:
                 pass
            placeholder = st.empty()
            for chunk in stream:
                delta = chunk.get("message", {}).get("content", "")
                response += delta
                placeholder.markdown(response + "▌")
            placeholder.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

            # 🔊 Browser TTS
            b64 = base64.b64encode(response.encode()).decode()
            st.markdown(f"""
            <script>
            const msg = new SpeechSynthesisUtterance(atob('{b64}'));
            window.speechSynthesis.speak(msg);
            </script>
            """, unsafe_allow_html=True)

# ----------------- Voice Input Button -----------------

