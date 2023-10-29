import os
import openai

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = os.environ["OPENAI_API_KEY"]

# account for deprecation of LLM model
import datetime

# Get the current date
current_date = datetime.datetime.now().date()

# Define the date after which the model should be set to "gpt-3.5-turbo"
target_date = datetime.date(2024, 6, 12)

# Set the model variable based on the current date
if current_date > target_date:
    llm_model = "gpt-3.5-turbo"
else:
    llm_model = "gpt-3.5-turbo-0301"

from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import CSVLoader
from langchain.vectorstores import DocArrayInMemorySearch
from IPython.display import display, Markdown


from langchain.document_loaders import Docx2txtLoader

loader = Docx2txtLoader("jerryGYM.docx")
# file = "outdoorclothing_catalog.csv"
# loader = CSVLoader(file_path=file)

from langchain.indexes import VectorstoreIndexCreator

# index = VectorstoreIndexCreator(vectorstore_cls=DocArrayInMemorySearch).from_loaders(
#     [loader]
# )

# index = VectorstoreIndexCreator().from_loaders([loader])
query = " What is the Membership Model of YOur GYM"

response = index.query(query)
print(response)
# print(type(response))
# mark_string = Markdown(response)
# print(mark_string)
# # display(Markdown(response))
# docs = loader.load()
# print(docs[0])

# from langchain.embeddings import OpenAIEmbeddings
# embeddings = OpenAIEmbeddings()#
# above one is the Implementation by Abstraction that whatever the question you can ask with YOur document.
# Now From here is the step by step Implementation of the above code.
