import os

import streamlit as st
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
model_name = os.environ.get("GEMINI_MODEL", "gemini-1.5-pro-latest")

# Set up the LLM
llm = ChatGoogleGenerativeAI(
    model=model_name, temperature=0.5, google_api_key=api_key
)

# Define the chains
# First chain: Generate restaurant name
prompt_name = PromptTemplate(
    input_variables=["cuisine"],
    template="I want to open a {cuisine} restaurant. Suggest a single fancy name.",
)
name_chain = prompt_name | llm | StrOutputParser()

# Second chain: Generate menu items
prompt_items = PromptTemplate(
    input_variables=["restaurant_name"],
    template="Suggest menu items for {restaurant_name}. Result should be a comma separated list.",
)
items_chain = prompt_items | llm | StrOutputParser()

# Combine chains using LCEL
sequential_chain = RunnablePassthrough.assign(
    restaurant_name=name_chain
).assign(menu_items=items_chain)

# Streamlit App
st.title("Restaurant Name and Menu Generator")

st.sidebar.header("Cuisine Selection")
cuisine = st.sidebar.selectbox(
    "Please pick a cuisine",
     [
         "Indian", "Italian", "Mexican", "Chinese",
         "American", "French", "Japanese", "Korean",
          "Mediterranean", "Thai", "Spanish", "Greek",
          "Vietnamese", "Lebanese", "Turkish", "Caribbean",
     ]
)

if st.sidebar.button("Generate"):
    with st.spinner("Generating..."):
        result = sequential_chain.invoke({"cuisine": cuisine})
        st.subheader("Restaurant Name:")
        st.write(result["restaurant_name"])
        st.subheader("Menu Items:")
        menu_items = [item.strip() for item in result["menu_items"].split(",")]
        for item in menu_items:
            st.write(f"- {item}")