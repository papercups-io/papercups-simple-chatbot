import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

print('creating embedding')
embed = hub.load("universal-sentence-encoder_4")

# def similarity():
questions_0 = open("questions/v0.txt", "r").read().split("\n")
questions_1 = open("questions/v1.txt", "r").read().split("\n")
questions_2 = open("questions/v2.txt", "r").read().split("\n")
questions_3 = open("questions/v3.txt", "r").read().split("\n")

questions = [
    questions_0,
    questions_1,
    questions_2,
    questions_3,
]

print("finished loading")
similarities = np.inner(embed(questions_0),embed(questions_1))


scores = []

for i in range(len(similarities)):
    s = similarities[i]
    j = np.argmax(s)
    score = s[j]
    # print("score", score)
    
    q0 = questions_0[i]
    q1= questions_1[j]
    # print(q0)
    # print(q1)
    # print("\n")
    scores.append({'score': score, 'q0': q0, 'q1': q1})


scores.sort(key=lambda x: x['score'])
for score in scores:
    if(score['score'] > 0.42):
    # print('score',score['score'])
        print(score['q0'])
        print(score['q1'])
        print("\n")
# print(scores)


# import pdb; pdb.set_trace()

# import pdb; pdb.set_trace()
# body = json.loads(request.data)
# embeddings = embed(body['text'])
# a,b = embeddings
# corr = np.inner(a, b)
# return {"cosine_similarity": str(corr)}
