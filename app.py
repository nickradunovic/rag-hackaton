import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import SimpleDirectoryReader

# Configure the Streamlit UI
st.set_page_config(
    page_title="<enter title>",  # <- enter a suitable title for your application
    page_icon="🦙",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)
st.title = ("<enter title>",)  # <- enter a suitable title for your application
st.info(
    "Check out the full tutorial to build this app in our [blog post](https://blog.streamlit.io/build-a-chatbot-with-custom-data-sources-powered-by-llamaindex/)",
    icon="📃",
)

# Use the OpenAI API key to access OpenAI's models.
openai.api_key = st.secrets.openai_key  # TODO: add key to secrets.toml

# NOTE: Use session_state to keep track of your chatbot's message history. see: https://docs.streamlit.io/library/api-reference/session-state?ref=blog.streamlit.io
if "messages" not in st.session_state.keys():  # Initialize the chat messages history
    st.session_state.messages = [{"role": "assistant", "content": "Ask me a question!"}]


@st.cache_resource(show_spinner=False)
def load_data():
    # TODO:
    # ...
    # - Use SimpleDirectoryReader to pass LlamaIndex the folder where you’ve stored your data (NOTE: create folder and put external data in).
    # - Create an instance of LlamaIndex’s ServiceContext to interact with LlamaIndex.
    # - Use VectorStoreIndex and SimpleVectorStore to structure your data in a way that helps your model quickly retrieve context from your data.
    # - Return a VectorStoreIndex object to be called 'index'
    # ...
    return index


index = load_data()

# TODO
if "chat_engine" not in st.session_state.keys():
    # Initialize the chat engine (NOTE: There are several different modes of chat engines)
    pass  # ...


# TODO: Prompt for user input and save to chat history
# ...
# if prompt := st.chat_input("Your question"):  # Prompt for user input and save to chat history
# st.session_state.messages.append({"role": "user", "content": prompt})

# TODO: Display the prior chat messages
# ...
for message in st.session_state.messages:  # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message)  # Add response to message history
