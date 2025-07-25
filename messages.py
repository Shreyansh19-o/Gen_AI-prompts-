from langchain_core.messages import AIMessage, HumanMessage,SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model= ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.2,max_tokens=50)

messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)
