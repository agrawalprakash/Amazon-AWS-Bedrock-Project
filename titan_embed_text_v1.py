import boto3
import json

from similarity import cosineSimilarity

client = boto3.client(service_name='bedrock-runtime',
                       region_name='us-west-2')

facts = [
          'The first computer was invented in 1938',
          'John Kennedy was the 35th President of the United States',
          'The first moon landing was in 1969',
           'The capital of India is New Delhi',
           'Mars is the fourth planet from Sun'
        ]

newFact = 'I like to play computer game'

def getEmbedding(input: str):
    response = client.invoke_model(
                body=json.dumps({
                  "inputText": input,
                }),
                modelId='amazon.titan-embed-text-v1',
                accept='application/json',
                contentType='application/json'
                )
     response_body = json.loads(response.get('body').read())   
     return response_body.get('embedding')

