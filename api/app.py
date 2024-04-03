from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv


load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server"
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

model=ChatOpenAI()

# ollama llama2
llm=Ollama(model="llama2")

prompt1=ChatPromptTemplate.from_template("Write me a 100 word essay about {topic}.")

prompt2=ChatPromptTemplate.from_template("Write me a 100 word poem about {topic}.")

add_routes(
    app,
    prompt1|model,# openai api
    path="/essay"
)

add_routes(
    app,
    prompt2|llm,# openai api
    path="/poem"
)


if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8080)