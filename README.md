# AI Chatbot

## Overview
This AI Chatbot is a Streamlit-based web application that allows users to ask questions and receive responses. It first attempts to match user queries with predefined answers from a dataset (`questions.json`). If no match is found, it uses MetaAI to generate a response.

## Features
- **Predefined Responses:** Uses fuzzy matching to find the closest predefined answer.
- **AI-Powered Responses:** If no match is found, it queries MetaAI for a response.
- **Chat History:** Displays the conversation history for a better user experience.
- **User-Friendly UI:** Uses custom styles for better chat formatting.
- **Logging:** Saves all questions and responses to `all_questions_answers.txt`.
- **Streamlit-Based:** Runs as a web application using Streamlit.

## How It Works
1. **Load Dataset:** Loads `questions.json` containing predefined questions and responses.
2. **User Input:** The user enters a question in the chat input field.
3. **Matching Process:**
   - If a similar question exists in the dataset (using fuzzy matching), the predefined response is returned.
   - If no match is found, the chatbot queries MetaAI to generate an answer.
4. **Display Response:**
   - Shows "Thinking..." while processing the response.
   - Displays the final response in a styled chat window.
5. **Logging:** The question and response are logged in `all_questions_answers.txt`.

## Modules Used
### 1. **Streamlit**
   - Provides a simple way to build web applications.
   - Used for UI components like input fields, buttons, and displaying messages.
   - Install using: `pip install streamlit`

### 2. **MetaAI API**
   - Used to generate AI-powered responses when no predefined answer is found.
   - Install using: `pip install meta-ai-api`

### 3. **RapidFuzz**
   - Enables fuzzy matching to find the closest predefined question.
   - Helps in improving the accuracy of responses.
   - Install using: `pip install rapidfuzz`

### 4. **JSON**
   - Used for storing and loading predefined questions and answers.
   - Helps in managing structured data efficiently.

## Installation & Setup
### Prerequisites
- Python 3.8+
- Required modules (install with the steps below)

### Install Dependencies
```sh
pip install streamlit meta-ai-api rapidfuzz
```

### Run the Chatbot
```sh
streamlit run chatbot.py
```

## File Structure
```
├── chatbot.py              # Main chatbot script
├── questions.json          # Predefined questions and responses
├── all_questions_answers.txt # Log file for storing Q&A
├── README.md               # Project documentation
```

## Usage
1. Run the chatbot.
2. Type a question in the input field.
3. Wait for "Thinking..." to process your query.
4. Receive a response from either the predefined dataset or MetaAI.
5. Continue chatting!



