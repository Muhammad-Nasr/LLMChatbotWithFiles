import streamlit as st  # Library for building web apps
from dotenv import load_dotenv  # Library for loading environment variables
from helper import (
    get_api_key,
    process_files,
    split_doc_chunks,
    get_vectorstore,
    get_conversation_chain,
    handle_userinput,
)
import time  # Library for working with time


def main():
    """
    Main function to set up the Streamlit app and handle user interactions.
    """
    load_dotenv()  # Load environment variables from .env file

    st.set_page_config(
        page_title="BotChat with multiple Files", page_icon=":books:"
    )  # Set page title and icon

    # Display initial information and instructions
    info = st.markdown(
        """
        Want to chat with your files? **Upload many files as you want** in (pdf, csv, docx, txt). 
        This tool is meant to help you chat with your files, based on the context of the files.

        This tool is using **LLM** powered by  LangChain and OpenAI.

        View Source Code on GitHub: https://github.com/Muhammad-Nasr/LLMChatbotWithFiles.git

        Feel free to use the code, develop it for your use, make it better!
        """
    )
    
    # Initialize session state variables
    if "messages" not in st.session_state:
        st.session_state.messages = []  # Store chat messages
    if "conversation" not in st.session_state:
        st.session_state.conversation = {}  # Store conversation data
    if "has_file" not in st.session_state:
        st.session_state.has_file = False  # Flag indicating if files are uploaded

    # Display chat header
    st.header("LLMBot Chat with Your Files :books:")

    # Display existing chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Handle user input prompt
    if prompt := st.chat_input("Chat with your files?"):
        if not st.session_state.has_file:
            st.warning("You Should Process File First", icon="🔥")
        else:
            info.empty()  # Clear info information
            st.session_state.messages.append(
                {"role": "user", "content": prompt}
            )  # Add user message to chat history
            handle_userinput(prompt)  # Process user input

    # Sidebar for file upload and settings
    with st.sidebar:
        # Retrieve OpenAI API key
        openai_api_key = get_api_key() 

        if not openai_api_key:
            st.warning(
                'Please insert OpenAI API Key. Instructions [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)', icon="⚠️")
        st.subheader("Your documents")
        
        # select type of document source
      
        files = st.file_uploader(
            "Upload your File here and click on 'Process'",
            accept_multiple_files=True,
            type=[".txt", ".pdf", ".csv", ".docx", "doc"])
        
        
        if files:
            if not openai_api_key:
                st.info(
                    "Files uploaded, But You should add open api key to chat with file!",
                    icon="⚠️")
                return
            
            if st.button("Process"):
                with st.spinner("Processing"):
                    
                    # get documents
                    document = process_files(files) 
                     # Split documents into chunks
                    docs = split_doc_chunks(document)
                    
                    # Create a vector store for efficient retrieval
                    vectorestore = get_vectorstore(docs, openai_api_key)
                    
                    # Create a conversational chain, combining a language model with the vector store
                    st.session_state.conversation = get_conversation_chain(
                        vectorestore, openai_api_key)
                
                    # Delay for visual effect
                    time.sleep(2)
                    
                    st.success(
                        "Files Uploaded Successfully, You can start chat now", icon="✅")

                    # file u
                    st.session_state.has_file = True

        else:
            # Delete all the items in session state if no files are uploaded or the user removed the files.
            for key in st.session_state.keys():
                del st.session_state[key]
                    
                    


if __name__ == '__main__':
    main()
