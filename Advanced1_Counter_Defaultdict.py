#Counter
from collections import Counter


l = [7,8,87,87,87,8,7,7,8,8,78,8,7,8,7,8,7,87,87,87,87,8,7,7,78,7,7,87,878,8,8,78,8,8]
print(Counter(l))
print(Counter('asdasdsadasdsadsadasdsadasdasda'))

s1 = 'How many letters appear in this phrase?'
print(Counter(s1))
s2 = 'How many words appear in this phrase ? 7 words ?'
print(Counter(s2.split()))
c = Counter(s2.split())
print(c.most_common(4))
print(c.values())
print(c.items())

#Defaultdict
from collections import defaultdict
d = {}
# Can't d{'one'} = 1

d2 = defaultdict(object)
d2['one'] = 1
print(d2)
d2['two']
print(d2)
d3 = defaultdict(lambda:32)
d3['one']
d3['two']
d3['three']
print(d3)
