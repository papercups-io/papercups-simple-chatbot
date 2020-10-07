from fastapi import Request, FastAPI
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import json

app = FastAPI()

print('starting to load model')
embed = hub.load("models/universal-sentence-encoder_4")
print('finished loading model')


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/similarities')
async def similarities(request: Request):
    body = await request.body()
    embeddings = embed(json.loads(body)['text'])
    a,b = embeddings
    corr = np.inner(a, b)
    return {"cosine_similarity": str(corr)}