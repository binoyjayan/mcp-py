import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
model_name = os.environ.get("GEMINI_MODEL", "gemini-1.5-pro-latest")

def main():
    llm = ChatGoogleGenerativeAI(
        model=model_name, temperature=0.5, google_api_key=api_key
    )

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

    result = sequential_chain.invoke({"cuisine": "American"})
    print(result)

if __name__ == "__main__":
    main()
