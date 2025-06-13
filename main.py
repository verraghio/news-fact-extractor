import getpass
import os
from langchain_groq import ChatGroq
from IPython.display import Markdown

if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ") 

def extract_facts_from_article(article: str):
    # Initialize the model
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

    # Create the prompt
    prompt = f""" You are an assistant helping with news analysis. Your task is to carefully read the following news article and extract all **verifiable facts** it presents.

    Please list the facts clearly and concisely using markdown bullet points. Avoid opinions, speculation, or analysis — only include factual information mentioned explicitly in the article.

    ### Output Format:
    ### Facts
    - Fact 1
    - Fact 2
    - Fact 3
    ...

    ### Article:
    {article}
    """

    # Invoke the model and return the result
    response = llm.invoke(prompt)
    print(response)


testNewsArticle = []
extract_facts_from_article(testNewsArticle)

