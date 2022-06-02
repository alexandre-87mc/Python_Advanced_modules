#Python Debbuger - pdb
import pdb
x = [1,2,3]
y = 2
z = 3

result = z+y
print(result)

#pdb.set_trace()     #Enter in this point to debbug

#result2 = x+result
#print(result2)

#Timeit - measuring code time
import timeit
#Create list '0-1-2-3-4...99'
'-'.join(str(n) for n in range(100))
print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
print(timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000))
print(timeit.timeit('"-".join(map(str, range(100)))', number=10000))

#Try Line profiler librarie