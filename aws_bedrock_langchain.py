# langchain
# langchain-community
from langchain_community.llms import Bedrock
import boto3

AWS_REGION = "us-west-2"

bedrock = boto3.client(
            service_name = "bedrock-runtime",
            region_name = AWS_REGION
          )

model = Bedrock(model_id = "amazon.titan-text-express-v1",
                client = bedrock)

def invoke_model():
    response = model.invoke("What is the highest mountain in the world?")
    print(response)

def fist_chain():
    template = ChatPromptTemplate.from_messages(
            [
              "system",
              def first_chain():
                   prompt = PromptTemplate.from_template(
                              "Write a short product description for: {product_name}"
                             )
                   chain = prompt | model

                   response = chain.invoke(
                                {"product_name":"bicycle"}
                              )
                   print(response)
            ]
    )

invoke_model()
fist_chain()
