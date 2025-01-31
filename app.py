import os
import openai
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st

def initialize_app():
    try:
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        
        if not api_key:
            raise ValueError("OPENAI_API_KEY is not set in .env file")
            
        return openai.OpenAI(api_key=api_key)
    except Exception as e:
        st.error(f"Initialization failed: {str(e)}")
        return None
    
sql_prompt = PromptTemplate(
    input_variables=["query"],
    template="""
    Convert this natural language query to SQL. Follow these rules:
    1. Use MySQL syntax
    2. Assume these tables exist:
       - products (id, name, price)
       - sales (id, product_id, amount, sale_date)
    3. Use proper aliases
    4. Format for readability
    
    Query: {query}
    
    SQL Query:
    """
)


def generate_sql(client, natural_language_query):
    try:
        if not natural_language_query.strip():
            raise ValueError("Query cannot be empty")
            
        formatted_prompt = sql_prompt.format(query=natural_language_query)
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": formatted_prompt}],
            max_tokens=150,
            temperature=0.3
        )
        
        return response.choices[0].message.content.strip()
    except Exception as e:
        st.error(f"Error generating SQL: {str(e)}")
        return None


def main():
    st.title("🔍 Natural Language to SQL Converter")
    st.markdown("Convert plain English questions to SQL queries")
    
    client = initialize_app()
    if not client:
        return
        
    query = st.text_area("Enter your question:", 
                       placeholder="e.g., Show total sales for each product last month",
                       height=100)
    
    if st.button("Generate SQL"):
        with st.spinner("Generating SQL..."):
            sql_query = generate_sql(client, query)
            
            if sql_query:
                st.subheader("Generated SQL")
                st.code(sql_query, language="sql")
                
                # Add copy button
                st.markdown(f"""
                ```html
                <button onclick="navigator.clipboard.writeText(`{sql_query}`)">
                    Copy SQL
                </button>
                """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()