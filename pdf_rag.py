from langchain_community.llms import Bedrock
from langchain_community.embeddings import BedrockEmbeddings
from langchain_community.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import boto3


question = "What themes does Gone with wind explorer?"

loader = PyPDFLoader("assets/books.pdf")
splitter = RecursiveCharacterTextSplitter(separator=["\n"])

docs = loader.load()
splitted_docs = splitter.split_documents(docs)


vector_store = FAISS.from_documents(splitted_docs, bedrock_embeddings)


retriever = vector_store.as_retriever(
                search_kwargs= {"k": 2}
            )

results = retriever.get_relevant_documents(question)





