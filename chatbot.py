import json
import streamlit as st
from meta_ai_api import MetaAI
from rapidfuzz import process

# Initialize MetaAI
ai = MetaAI()

# Load predefined questions
@st.cache_data
def load_dataset():
    with open('questions.json', 'r') as file:
        dataset = json.load(file)

    # Convert dataset to a dictionary for fast lookups
    questions_dict = {item["question"].lower(): item["response"] for item in dataset}
    return dataset, questions_dict

dataset, questions_dict = load_dataset()

# Function to find best response using fuzzy matching
def find_response(user_query):
    match = process.extractOne(user_query.lower(), questions_dict.keys(), score_cutoff=80)
    if match:
        best_match = match[0]
        return questions_dict[best_match]
    return None

# Function to query MetaAI if no match is found
def get_meta_ai_response(user_query):
    dataset_string = json.dumps(dataset)
    prompt_message = f"Use only the given dataset to answer the question. Do not make up answers.\nDataset: {dataset_string}\nQuestion: {user_query}"
    
    response = ai.prompt(message=prompt_message)
    return response.get('message', "I'm sorry, I couldn't find an answer for that question.")

# Logging function
def log_question_and_response(question, response):
    with open("all_questions_answers.txt", "a") as log_file:
        log_file.write(f"Question: {question}\nResponse: {response}\n\n")

# Custom CSS for better UI
st.markdown("""
    <style>
        .user-msg { 
            background-color: #0078d4; 
            color: white; 
            padding: 10px; 
            border-radius: 10px; 
            margin: 5px 0; 
            max-width: 70%; 
            margin-left: auto; 
            margin-right: 10px; 
            box-shadow: 0 2px 4px rgba(0,0,0,0.1); 
        }
        .bot-msg { 
            background-color: #f1f1f1; 
            color: black; 
            padding: 10px; 
            border-radius: 10px; 
            margin: 5px 0; 
            max-width: 70%; 
            margin-right: auto; 
            margin-left: 10px; 
            box-shadow: 0 2px 4px rgba(0,0,0,0.1); 
        }
        .chat-container { 
            max-width: 700px; 
            margin: auto; 
            padding: 20px; 
            background-color: #ffffff; 
            border-radius: 15px; 
            box-shadow: 0 4px 8px rgba(0,0,0,0.2); 
        }
        .stButton>button { 
            background-color: #0078d4; 
            color: white; 
            border-radius: 5px; 
            padding: 10px 20px; 
            border: none; 
            box-shadow: 0 2px 4px rgba(0,0,0,0.1); 
        }
        .stButton>button:hover { 
            background-color: #005bb5; 
        }
        .stTextInput>div>div>input { 
            border-radius: 5px; 
            padding: 10px; 
            border: 1px solid #ddd; 
            box-shadow: 0 2px 4px rgba(0,0,0,0.1); 
        }
        .stTitle { 
            color: #0078d4; 
            font-size: 2.5em; 
            text-align: center; 
            margin-bottom: 20px; 
        }
        .stMarkdown { 
            text-align: center; 
            color: #555; 
            margin-bottom: 30px; 
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit chatbot UI
def chatbot():
    st.title("💬 AI Chatbot")
    st.markdown("🚀 Ask me anything!", unsafe_allow_html=True)

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display chat history
    for entry in st.session_state.chat_history:
        st.markdown(f"<div class='user-msg'><b>You:</b> {entry['question']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='bot-msg'><b>Bot:</b> {entry['response']}</div>", unsafe_allow_html=True)

    # User input at the bottom
    user_query = st.chat_input("Type your question here...")

    if user_query:
        # Avoid re-processing same query to prevent duplicate display
        if "last_query" in st.session_state and st.session_state.last_query == user_query:
            st.stop()

        st.session_state.last_query = user_query

        # Show "Thinking..." message before fetching response
        with st.spinner("🤖 Thinking..."):
            response = find_response(user_query) or get_meta_ai_response(user_query)

        # Store conversation history
        st.session_state.chat_history.append({"question": user_query, "response": response})

        # Re-run app to display the updated response
        st.rerun()

if __name__ == "__main__":
    chatbot()
