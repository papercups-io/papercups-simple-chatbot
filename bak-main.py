from flask import Flask, request
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import json

app = Flask(__name__)

print('starting to load model')
embed = hub.load("models/universal-sentence-encoder_4")
print('finished loading model')

@app.route('/',)
def hello():
    return "yo"


@app.route('/similarity', methods=["POST"])
def similarity():
    body = json.loads(request.data)
    embeddings = embed(body['text'])
    a,b = embeddings
    corr = np.inner(a, b)
    return {"cosine_similarity": str(corr)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)