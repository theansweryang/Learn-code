import arcpy
import pandas as pd

res = [x for x in range(3)] #【variable (for loop with the variable)】
print(res)

print ([(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2])
#solve x**2+y**2=z**2 

S = [x**2 for x in range(10)]
V = [2**i for i in range(13)]
M = [x for x in S if x % 2 == 0]
print (S); print (V); print (M)

##sorted
strs = ['aa', 'BB', 'zz', 'CC']
print (sorted(strs))  
print (sorted(strs, reverse=True))   
strs = ['ccc', 'aaaa', 'd', 'bb']
print (sorted(strs, key=len))#根据单词长度排序
list_of_medals = [('Italy', 5), ('Russia', 10), ('Germany', 16),('Ireland', 10), ('Spain', 9), ('Albania', 8), ('Lithuania', 7), ('Iceland', 6), ('Sweden', 24), ('Malta', 5), ('Estonia', 4), ('Turkey', 4), ('Moldova', 2), ('Serbia', 4),  ('Azerbaijan', 2)]

sorted(list_of_medals, key=lambda tup: (-tup[1], tup[0]))#先按照数字倒排序，数字一样再按照阿拉伯正排序

##zip for list adding
x=[1,2,3]
y=[4,5,6]
z=[7,8,9]
xyz=zip(x,y,z)
list(xyz)
