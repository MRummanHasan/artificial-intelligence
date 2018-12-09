import math

BagOfWords = [[1, 1, 1, 1, 1, 0, 0],
              [1, 1, 1, 1, 0, 0, 1]
]

print("Collection of Sentences: \n",BagOfWords,"\n")
Q = [1, 1, 1, 1, 0, 0, 1]
v = 0
d = []
for row in BagOfWords:
    for i in range(len(row)):
        v += (row[i]-Q[i])**2
    v = math.sqrt(v)

    d.append(v)
    v = 0
print("Eucl distance per sentence:\n",d)

mostSimilar = min(d)
print()
print(BagOfWords[d.index(mostSimilar)],"most similar sentence")
print(mostSimilar)
