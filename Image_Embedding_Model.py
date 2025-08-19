import boto3
import json
import base64

from similarity import cosineSimilarity

client = boto3.client
         (
           service_name = 'bedrock-runtime',
           region_name = 'us-west-2'
         )

images = [
            'images/1.png',
            'images/2.png',
            'images/3.png'
         ]

def getImagesEmbedding(imagePath: str):
    with open(imagePath, "rb") as f:
      base_image = base64.b64encode(
                    f.read()).
                    decode("utf-8"))

      response = client.invoke_model(
        body = json.dumps(
          "input_image": base_image,
        )
        modelId = 'amazon.titan-embed-image-v1',
        accept = 'application/json',
        contentType = 'application/json'
      )
      response_body = json.loads
                      (response.get('body').read())
      return response_body.get('embedding')


      
