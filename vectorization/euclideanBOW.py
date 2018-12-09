import math
import pandas as pd

BagOfWords = [[1, 1, 1, 1, 1, 0, 0],
              [0, 1, 1, 1, 1, 0, 0],
              [0, 0, 0, 1, 1, 1, 0],
              [1, 1, 1, 1, 0, 0, 1]
              ]
print("Collection of Sentences: \n",pd.DataFrame(BagOfWords),"\n")
# or
# print("Collection of Sentences: \n",BagOfWords, "\n")

qeury = [1, 1, 1, 1, 0, 0, 1]

def eucl(BagOfWords,qeury):
    v = 0
    d = []
    for row in BagOfWords:
        for i in range(len(row)):
            v += (row[i]-qeury[i])**2
        
        v = math.sqrt(v)
        d.append(v)
        v = 0
    return d

d = eucl(BagOfWords,qeury)
print("Eucl distance per sentence:\n",pd.DataFrame(d))
# or
# print("Eucl distance per sentence:\n",d)

mostSimilar = min(d)
print()
print("Most similar sentence found is: ", BagOfWords[d.index(mostSimilar)])
print("with value of: ",mostSimilar)
print("at Index number: ",d.index(mostSimilar))
