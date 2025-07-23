from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage  
load_dotenv()

model= ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.2,max_tokens=50)

chat_history = [
    SystemMessage(content='You are a helpful assistant'),
    
]

while True:
    user_input=input('You : ')
    chat_history.append(HumanMessage(content= user_input))
    if user_input.lower() == 'exit':
        print("Exiting the chatbot. Goodbye!")
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content= result.content))
    print("AI:", result.content)

    
print(chat_history)