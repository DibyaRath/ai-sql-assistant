import streamlit as st
from sql_agent import generate_sql, run_query
from db import init_db

init_db()

st.title("🤖 AI SQL Assistant")

question = st.text_input("Ask your data question:")

if st.button("Run"):
    if question:
        sql = generate_sql(question)
        st.code(sql, language="sql")

        result = run_query(sql)

        st.write("### Result:")
        st.write(result)
