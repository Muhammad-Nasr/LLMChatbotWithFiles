# LLMChatbotWithFiles

**Chat with your files using a large language model (LLM)!**

***LLMChatbotWithFiles*** is a Streamlit app that lets you upload text files (PDF, CSV, DOCX, TXT), process them using a powerful LLM, and then chat with the files to extract insights, ask questions, and explore the knowledge within them. It's powered by OpenAI's LLM, LangChain's vectorstore technology, and Streamlit's user-friendly interface.

## Features

- **Upload multiple files:** Easily upload multiple text files in various formats.
- **AI-powered conversations:** Chat with your files using a large language model, capable of generating informative and insightful responses.
- **Knowledge extraction:** Uncover hidden knowledge and insights from your files through natural language conversations.
- **File chunking:** Optimizes processing and retrieval by splitting large documents into smaller chunks.
- **Vectorstore technology:** Leverages LangChain's vectorstore for efficient document storage and retrieval.
- **User-friendly interface:** Streamlit provides a simple and intuitive interface for easy interaction.

## Requirements

- **Python 10.0.0:** This app uses Python 10.0.0 to ensure compatibility with some packages.


## Getting Started

1. Clone this repository:

   ```bash
   git clone [https://github.com/Muhammad-Nasr/LLMChatbotWithFiles.git](https://github.com/Muhammad-Nasr/LLMChatbotWithFiles.git)
   ```
    > Use code with caution. Learn more

2. **Create a virtual environment:**

   It's highly recommended to create a virtual environment to isolate project dependencies:

   ```bash
   python -m venv env
   source env/bin/activate

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Obtain an OpenAI API key**:

   - Sign up for a free OpenAI account: https://beta.openai.com/
   Create a new API key and copy it.
   - Sign up for a free OpenAI account: https://beta.openai.com/
   Create a new API key and copy it.
   - Set your OpenAI API key as an environment variable:

   ``` Bash
   export OPENAI_API_KEY=your_api_key
   OPENAI_API_KEY=your key       # in .env file
   ```

5. **Run the app**:

   ```Bash
   streamlit run main.py
   ```

### Usage

1. Put your open api key in input.
2. Upload your files using the file uploader.
3. Click the "Process" button to process the files.
4. Start chatting with your files in the chat box.
5. The app will respond with insights and answers based on the  content of the files.

### References

* LangChain Documentation: https://langchain.readthedocs.io/
* Streamlit Documentation: https://docs.streamlit.io/

## Functionality

LLMChatbotWithFiles supports a range of tasks, including:

- **Question answering:** Ask specific questions about the content of your files, and the app will provide concise and informative answers.
- **Summarization:** Get a summary of key information and insights from your files, saving you time and effort in reading through lengthy documents.
- **Text generation:** Create new text based on the knowledge and patterns extracted from your files, such as generating creative text formats,  like poems, code, scripts, musical pieces, email, letters, etc.
- **Conversational exploration:** Engage in natural language conversations with the app to uncover hidden insights, explore connections between ideas, and deepen your understanding of the content.

## Examples

Here are some examples of how you can use LLMChatbotWithFiles:

1. **Question answering:**
   - Upload a research paper on machine learning.
   - Ask: "What are the key challenges in developing artificial general intelligence?"
   - The app might respond with: "Several challenges exist in developing AGI, including: achieving human-level understanding and reasoning, ensuring safety and controllability, aligning goals with human values, and overcoming hardware and data limitations."

2. **Summarization:**
   - Upload a lengthy report on climate change.
   - Ask: "Summarize the main findings and recommendations of the report."
   - The app might provide a succinct summary of the key points, saving you time in reading the entire report.

3. **Text generation:**
   - Upload a collection of poems by Emily Dickinson.
   - Ask: "Generate a new poem in a similar style to Emily Dickinson's work."
   - The app might create a poem that reflects the themes, patterns, and tone of Dickinson's poetry, showcasing its ability to understand and mimic literary styles.

4. **Conversational exploration:**
   - Upload a historical document about the American Revolution.
   - Engage in a conversation with the app to explore different perspectives, ask follow-up questions, and gain a deeper understanding of the events and motivations behind the revolution.

## Contact

For any inquiries or feedback, please reach out to:

- **Phone (Egypt):** (0020-11562-88555)
- **Email:** muhammadnasr.elsaid@gmail.com
- **LinkedIn:** [www.linkedin.com/in/muhmmad-nasr-8a2119236](www.linkedin.com/in/muhmmad-nasr-8a2119236)
- **Website:** [muhammadnasr.website](muhammadnasr.website)
- **GitHub:** [https://github.com/Muhammad-Nasr](https://github.com/Muhammad-Nasr)
