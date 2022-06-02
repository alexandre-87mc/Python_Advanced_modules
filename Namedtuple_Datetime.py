#Namedtuple
#Remembering tuples
t = (1,2,3)
print(t[0])

from collections import namedtuple
dog = namedtuple('Dog', 'age breed name')
sam = dog(age=2, breed='Huskie',name='Sam')
print(sam)
print(sam.age)

#Datetime
import datetime
t = datetime.time(4,20,1)
print(t)
print(datetime.time.max)
today = datetime.date.today()
print(today)
print(today.ctime())

#Operations with datetime
d1 = datetime.date(2015,3,11)
d2 = datetime.date(2011,3,11)
print(d1-d2)