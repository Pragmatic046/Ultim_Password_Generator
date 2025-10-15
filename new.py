import itertools 
from itertools import product


base = input ("write a word: ")
combo = set(map(''.join,itertools.product(*((c.lower(),c.upper()) for c in base))))

for a in combo:
    print(a)
    
    

# result = product(('a', 'A'),('b','B'),(1,2,3))
# print(list(result))

# unique_tuples = []
# seen = set()

# for t in [('a','B'), ('A','B'), ('a','B')]:
#     if t not in seen:
#         seen.add(t)
#         unique_tuples.append(t)

# print(unique_tuples, seen)

# base = input("word: ")

# combo = set(map(''.join, itertools.product(*((c.lower(), c.upper()) for c in base))))

# words = ["apple", "banana", "Apple"]
# unique_upper = set(map(str.upper, words))
# print(unique_upper)

# words = ['Hello', 'world', 'Python']
# sentence = ' '.join(words)
# print(sentence)
