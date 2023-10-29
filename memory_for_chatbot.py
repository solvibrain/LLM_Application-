import os
import openai

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory,ConversationBufferWindowMemory

llm = ChatOpenAI(temperature=0.0)
memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm, 
    memory = memory,
    verbose=True  # here If I want the Abstraction of the Implementation than I can simply use the verbose = True.
    # verbose=False
)
# print(conversation.predict(input="Hi, my name is Andrew"))
# print(memory.buffer) # this will show that How the previous conversation is stored in the buffer of a memory
# print(memory.load_memory_variables({})) # this gives the Dictionary of the History of the Conversatioin 

################## memory = ConversationBufferMemory() ####### It is quite costly because it store the whole conversation from the starting as gives the lLM as a Input by which tokenisation get increases and it will increase the cost of using the token.So ther eis other way of doinng this 

# @@@@@@@ memory = ConversationBufferWindowMemory() @@@@@@@@@@@@ # it stores on the basis of the window size that is given as a parameter of the value of K=1,3,5,6.....
llm = ChatOpenAI(temperature=0.0)
memory = ConversationBufferWindowMemory(k=3)
conversation = ConversationChain(
    llm=llm, 
    memory = memory,
    verbose=True  # here If I want the Abstraction of the Implementation than I can simply use the verbose = True.
    # verbose=False
)
# print(conversation.predict(input="Hi, my name is Andrew"))
# print(conversation.predict(input="I want you to help me in building by Study Timetable"))
# print(conversation.predict(input="yeah , I have Subjects = ['Maths','ENglish','SScience']"))
# print(conversation.predict(input="I want to Study Maths for about 3 hours and English for about 1 hr and SScience for about 1 hr"))
# print(conversation.predict(input = "I want to study aboyt 5 days in a week"))


from langchain.memory import ConversationTokenBufferMemory # here this is more cost effective because it will limit to the SEndig token by the User.
from langchain.llms import OpenAI
llm = ChatOpenAI(temperature=0.0)

memory = ConversationTokenBufferMemory(llm=llm, max_token_limit=30)
memory.save_context({"input": "AI is what?!"},
                    {"output": "Amazing!"})
memory.save_context({"input": "Backpropagation is what?"},
                    {"output": "Beautiful!"})
memory.save_context({"input": "Chatbots are what?"}, 
                    {"output": "Charming!"})

print(memory.load_memory_variables({}))

from langchain.memory import ConversationSummaryBufferMemory

# create a long string
schedule = "There is a meeting at 8am with your product team. \
You will need your powerpoint presentation prepared. \
9am-12pm have time to work on your LangChain \
project which will go quickly because Langchain is such a powerful tool. \
At Noon, lunch at the italian resturant with a customer who is driving \
from over an hour away to meet you to understand the latest in AI. \
Be sure to bring your laptop to show the latest LLM demo."

memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=100)
memory.save_context({"input": "Hello"}, {"output": "What's up"})
memory.save_context({"input": "Not much, just hanging"},
                    {"output": "Cool"})
memory.save_context({"input": "What is on the schedule today?"}, 
                    {"output": f"{schedule}"})

memory.load_memory_variables({})

conversation = ConversationChain(
    llm=llm, 
    memory = memory,
    verbose=True
)
conversation.predict(input="What would be a good demo to show?")

memory.load_memory_variables({})