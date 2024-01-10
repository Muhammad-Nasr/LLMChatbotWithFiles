
import streamlit as st  # Web framework for building interactive apps
import tempfile  # For creating temporary files
# Load documents from various formats
from langchain.document_loaders import (
    PyPDFLoader,
    TextLoader,
    CSVLoader,
    Docx2txtLoader,
)  
# Split text into chunks
from langchain.text_splitter import RecursiveCharacterTextSplitter
# Generate embeddings using OpenAI API
from langchain_openai import OpenAIEmbeddings
# Store and retrieve vectors efficiently
from langchain.vectorstores import FAISS

# Create conversational chains
from langchain.chains import ConversationalRetrievalChain  
# Use ChatOpenAI LLM for conversations
from langchain_openai import ChatOpenAI
# Access OpenAI API
import openai  
# get environment
import os

def get_api_key() -> str:
    """
    The user has two options, use env or input the key on the browser.
    Try to get the Open API key from env.
    Prompts the user for their OpenAI API key and validates it.

    Returns:
        str: The validated OpenAI API key or None if invalid.
    """

    env_api_key = os.getenv('OPENAI_API_KEY')
    # Create a text input for the user to enter their API key
    open_api_key = st.text_input(
        label="OpenAI API Key",
        placeholder="Ex: sk-2twmA8tfCb8un4...",
        key="openai_api_key_input",
    )
    
    # check option to use env or input in the browser
    if not open_api_key and env_api_key:
        open_api_key = env_api_key

    # Check if the entered API key starts with "sk-" (a valid OpenAI API key format)
    if not open_api_key.startswith("sk-"):
        return None  # Return None if the API key is not valid

    return open_api_key  # Return the validated API key



def process_files(docs: list[st.file_uploader]) -> list:
    """Processes uploaded files using appropriate document loaders.

    Args:
        docs: A list of uploaded files.

    Returns:
        list: A list of processed documents.
    """
    documents = []  # Create an empty list to store processed documents

    # Loop through each uploaded file
    for file in docs:
        # Determine the appropriate loader based on the file type
        if file.type == "application/pdf":
            Loader = PyPDFLoader
            
        elif file.endswith(".docx") or file.endswith(".doc"):
            Loader = Docx2txtLoader
            
        elif file.type == "text/csv":
            Loader = CSVLoader
            
        else:
            Loader = TextLoader

        # Create a temporary file to store the file contents
        with tempfile.NamedTemporaryFile(delete=False) as tf:
            tf.write(file.read())  # Write the file contents to the temporary file
            loader = Loader(tf.name)  # Create a loader instance using the temporary file
            documents.extend(loader.load())  # Load the documents using the loader and add them to the list

    return documents  # Return the list of processed documents


def split_doc_chunks(doc: list) -> list:
    """Splits a document into smaller chunks for efficient processing.

    Args:
        doc: A list of documents.

    Returns:
        list: A list of smaller chunks.
    """
    # Create a text splitter object with specific chunk size and overlap
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )

    # Split the documents into smaller chunks
    docs = text_splitter.split_documents(doc)

    return docs  # Return the list of smaller chunks


def get_vectorstore(
    docs: list, open_api_key: str) -> FAISS:  # Specify return type for clarity
    """Creates a vector store for the documents using OpenAI embeddings.

    Args:
        docs: A list of processed documents.
        open_api_key: The OpenAI API key.

    Returns:
        FAISS: The created vector store.
    """
    try:
        # Create an object to generate text embeddings using the OpenAI API
        embeddings = OpenAIEmbeddings(api_key=open_api_key)

        # Build the vector store using the documents and embeddings
        vectorstore = FAISS.from_documents(docs, embeddings)

        return vectorstore  # Return the built vector store

    except openai.APIError as e:
        # Handle any errors from the OpenAI API
        print(f"OpenAI API returned an API Error: {e}")
        st.warning(f"OpenAI API returned an API Error: {e}")
        st.stop()  # Stop the Streamlit app if an error occurs


def get_conversation_chain(vectorstore, open_api_key):
    """
    Creates a conversational chain, combining a large language model (LLM) with the vector store.

    Args:
        vectorstore: The vector store containing processed documents.
        open_api_key: The user's OpenAI API key for accessing the LLM.

    Returns:
        ConversationalRetrievalChain: The created conversational chain, ready for interaction.
    """

    try:
        # Create an LLM (ChatOpenAI) instance for conversation
        llm = ChatOpenAI(temperature=0, api_key=open_api_key)


        # Build the conversational chain using the LLM, retriever, and memory
        chain = ConversationalRetrievalChain.from_llm(
            llm=llm, retriever=vectorstore.as_retriever(), 
        )

        return chain  # Return the created conversational chain

    except openai.APIError as e:
        # Handle any errors from the OpenAI API
        print(f"OpenAI API returned an API Error: {e}")
        st.warning(f"OpenAI API returned an API Error: {e}")
        st.stop()  # Stop the Streamlit app if an error occurs


def handle_userinput(prompt):
    """
    Handles user input and generates a response using the conversational chain.

    Args:
        prompt: The user's input text.
    """

    try:
        # Display the user's input in the chat interface
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate a response using the conversational chain
        with st.chat_message("assistant"):
            message_placeholder = st.empty()  # Create a placeholder for the response
            response = ""

            # Get the response from the conversational chain, pass empty chat history, it is required.
            response = st.session_state.conversation({"question": prompt,
                                                      "chat_history":[]})
            response = f"**{response['answer']}**"  # Format the response

            # Display the response in the chat interface
            message_placeholder.markdown(response, unsafe_allow_html=True)

            # Store the response in the conversation history
            st.session_state.messages.append(
                {"role": "assistant", "content": response})

    # handle any error with open ai key
    except openai.APIError as e:
        # Handle any errors from the OpenAI API
        #print(f"OpenAI API returned an API Error: {e}")
        st.warning(f"OpenAI API returned an API Error: {e}")
        st.stop()










