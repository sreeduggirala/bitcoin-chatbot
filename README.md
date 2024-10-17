# Bitcoin Whitepaper Chatbot

This repository contains a Retrieval-Augmented Generation (RAG) based chatbot designed to answer questions about the Bitcoin whitepaper. 

## What is RAG?

Retrieval-Augmented Generation (RAG) is a technique that combines the strengths of information retrieval and natural language generation to provide more accurate and contextually relevant responses. 

In the context of this chatbot, RAG works by first using vector embeddings to represent the chunks of the Bitcoin whitepaper in a high-dimensional space. These embeddings are stored in a vector database like ChromaDB. When a user asks a question, the system performs a semantic search to retrieve the most relevant chunks of text based on their vector similarity to the query. 

These retrieved chunks are then fed into a language model, such as GPT-4o-Mini, which generates a coherent and informative response by leveraging the context provided by the retrieved information.


## Installation

To set up the project, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/bitcoin-chatbot.git
    cd bitcoin-chatbot
    ```

2. **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    Create a `.env` file in the root directory and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

## Running the Chatbot

To run the chatbot, execute the following command:

```bash
python src/main.py
```

This will start the chatbot, and you can interact with it through the terminal or a web interface if implemented.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
