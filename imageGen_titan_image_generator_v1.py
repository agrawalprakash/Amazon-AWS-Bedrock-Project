import boto3
import json
import base64

client = boto3.client(
            service_name='bedrock_runtime',
            region_name='us-west-2'
          )

def get_configuration(inputImage: str):
    return json.dumps({
      "taskType": "INPAINTING",
      "inPaintingParams": {
          "text": "Make the cat black and blue",
          "negativeText": "bad quality, low resolution",
          "image": inputImage,
          "maskPrompt": "cat"
        },
        "imageGenerationConfig": {
            "numberOfImages": 1,
            "height": 512,
            "width": 512,
            "cfgScale": 8.0,
          }
})

with open("cat.png", "rb") as f:
  base_image = base64.b64encode(f.read()).decode("utf-8")

async function invokeModel() {
    const image = readImage('cat.png');
    const config = get_configuration(image);
    const response = 
      await client.send(new InvokeModelCommand({
        modelId: 'amazon.titan-image-generator-v1',
          body:  JSON.stringify(config),
        accept: 'application/json',
        contentType: 'application/json'
        }));

const responseBody = JSON.parse
                     (new TextDecoder().decode(response.body));

saveImage(responseBody.images[0], 'catEdited.png')

        
