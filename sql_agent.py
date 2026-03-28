from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
import sqlite3

llm = ChatOpenAI(temperature=0)

prompt = PromptTemplate(
    input_variables=["question"],
    template="""
You are an expert SQL assistant.

Convert the following question into SQL query for SQLite.

Table: sales(id, customer, amount, date)

Rules:
- Only return SQL
- Do not explain

Question: {question}
"""
)

def generate_sql(question):
    formatted_prompt = prompt.format(question=question)
    response = llm.predict(formatted_prompt)
    return response.strip()

def run_query(query):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except Exception as e:
        result = str(e)

    conn.close()
    return result
