import streamlit as st
import snowflake.connector

ctx = snowflake.connector.connect(
    user= 'STREAMLITTEST',
    password='JanRam@2023',
    account='jzjfmqu-eob02451',
    warehouse='Compute_WH',
    role='ACCOUNTADMIN',
    database='PETS',
    schema ='PUBLIC'
    )
cs = ctx.cursor()

# Initialize connection.
# Uses st.cache_resource to only run once.


# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    cs.execute(query)
    return cs.fetchall()

rows = run_query("SELECT * from mytable;")





