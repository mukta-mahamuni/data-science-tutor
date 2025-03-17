import streamlit as st
from utils import initialize_gemini

# Initialize session state for conversations
if 'conversations' not in st.session_state:
    st.session_state.conversations = {}
if 'active_chat' not in st.session_state:
    st.session_state.active_chat = None

# Function to create a new chat session
def start_new_chat():
    new_chat_id = f"chat_{len(st.session_state.conversations) + 1}"
    st.session_state.conversations[new_chat_id] = []
    st.session_state.active_chat = new_chat_id
    st.session_state.conversation = initialize_gemini()

# Sidebar for chat history and controls
with st.sidebar:
    st.title("💬 Chat History")
    
    # Display previous chats
    for chat_id in st.session_state.conversations:
        if st.button(f"📂 {chat_id}", key=chat_id):
            st.session_state.active_chat = chat_id
            st.session_state.conversation = initialize_gemini()

        # Option to delete a chat
        if st.button(f"❌", key=f"delete_{chat_id}"):
            del st.session_state.conversations[chat_id]
            if st.session_state.active_chat == chat_id:
                st.session_state.active_chat = None
                st.session_state.conversation = None

    st.divider()

    # Start a new chat button
    if st.button("➕ Start New Chat"):
        start_new_chat()

# Main chat interface
st.title("🤖 Conversational AI Data Science Tutor")

# Active chat setup
if st.session_state.active_chat:
    current_chat = st.session_state.conversations[st.session_state.active_chat]

    # Display chat history
    for msg in current_chat:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**AI:** {msg['content']}")

    # Chat input for user message
    user_input = st.chat_input("Ask a Data Science question...")
    if user_input:
        # Display user message
        current_chat.append({"role": "user", "content": user_input})
        st.markdown(f"**You:** {user_input}")

        # Generate AI response
        response = st.session_state.conversation.run(user_input)

        # Display AI response and store in chat
        current_chat.append({"role": "assistant", "content": response})
        st.markdown(f"**AI:** {response}")

else:
    st.write("👉 Start a new chat from the sidebar!")

