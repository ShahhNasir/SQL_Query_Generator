# Natural Language to SQL Converter

Convert plain English questions into SQL queries using OpenAI's GPT-4.

## Features
- 🚀 **Natural Language Input**: Ask questions in plain English.
- 💻 **SQL Output**: Get properly formatted SQL queries.
- 📋 **Copy to Clipboard**: One-click copy for generated SQL.
- 🌐 **Web Interface**: Easy-to-use web app built with Streamlit.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ShahhNasir/SQL_Query_Generator.git
   cd SQL_Query_Generator

2. Install dependencies:
    '''bash
    pip install -r requirements.txt
3. Add your OpenAI API key:
    Create a .env file in the project root.
    Add the following line:
    OPENAI_API_KEY=your_api_key_here
4. Run the app:
    streamlit run app.py