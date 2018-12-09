import math

s1 = [1, 1, 1, 1, 1, 0, 0]
q1 = [1, 1, 1, 1, 0, 0, 1]
v = 0

for i in range(len(s1)):
    v += (s1[i]-q1[1])**2
print(math.sqrt(v))


# min(d[])
