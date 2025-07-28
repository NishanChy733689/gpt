import streamlit as st
from ollama import chat

# Sidebar setup
with st.sidebar:
    st.title("🤖💬 Ollama Chatbot")

    # List all downloaded models
    models = ["qwen2.5-coder:1.5b","gemma3:1b","phi:latest","qwen3:0.6b"]

    if not models:
        st.error("No models found in Ollama. Use `ollama run <model>` to download one.")
        st.stop()

    # Model selection
    model = st.selectbox("Choose a model", models)
    st.success(f"Using model: {model}")

# Session state initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display message history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# Prompt input
if prompt := st.chat_input("Your message"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    full_response = ""
    placeholder = st.chat_message("assistant").empty()

    # Stream response from Ollama
    stream = chat(
        model=model,
        messages=st.session_state.messages,
        stream=True
    )

    for chunk in stream:
        delta = chunk.get("message", {}).get("content", "")
        full_response += delta
        placeholder.markdown(full_response + "▌")

    placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
