import os
import pandas as pd
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GEMINI_API_KEY)
llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash', api_key=GEMINI_API_KEY)

def csv_agent(input_file, question: str) -> str:
    df = pd.read_csv(input_file)
    agent = create_pandas_dataframe_agent(
        llm,
        df,
        # verbose=True,
        allow_dangerous_code=True
    )
    result = agent.invoke(question)
    return result["output"]