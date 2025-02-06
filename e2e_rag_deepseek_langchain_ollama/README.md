# Project 1
## End to end RAG with Langchain and Deepseek for Ollama
* https://chat.deepseek.com/

#### Ollama
##### Installation
* Go to [Ollama Website](https://ollama.com/)
* Click **Download** and select **Download for Windows**
* Save the **Ollama.exe** file to your computer
* Run the **Ollama.exe** file to install Ollama

#### Install and Run Ollama for Deepseek
* Download the Ollama for Deepseek from the [Ollama website](https://ollama.com/search?q=deepseek)
* Go to the website and select **deepseek-r1** 
* Choose the **1.5b** model
* Open a command prompt window and run the following command:
  * I had issues running this in a PoweShell window, so I used the command prompt as I was getting question marks in the output
  * I think this is due to the encoding of the output
```commandline
ollama run deepseek-r1:1.5b
```
* The first time you run this command, it will download the model and then run it in the command prompt window

### Run the End to End RAG with Langchain and Deepseek
* Create a new conda environment
```bash
conda create -n e2e_rag_deepseek_langchain_ollama python=3.8
conda activate e2e_rag_deepseek_langchain_ollama
```

* Install the required packages
```bash
pip install -r requirements.txt
```

### Project Structure
* The project is split into two parts 
* The first is a general Question Answering system using the RAG model
* Run the main.py file to start the Question Answering system
```bash
streamlit run main.py
```
* Below is the folder structure for the project
```plaintext
qa/
│
├── main.py
├── chat_engine.py
├── ui_components.py
└── prompt_builder.py
```

* The second part is the End to End RAG with Langchain and Deepseek to read and answer from PDFs
* The app uploads the pdf, reads it and then answers questions from the text
* Run the main.py file to start the End to End RAG with Langchain and Deepseek
```bash
streamlit run main.py
```
* Below is the folder structure for the project
```plaintext
pdf_qa/
│
├── main.py
├── document_processing.py
├── ui_components.py
└── chat_engine.py
```