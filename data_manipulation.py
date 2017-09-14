
import pandas as pd
import numpy as np
m1 = pd.DataFrame(np.random.randint(0, 5,size=(5,5)))
m2 = pd.DataFrame(np.random.randint(0, 5,size=(5,5)))


"""matrix multification"""
m3=m1.dot(m2)
m4=m1.multiply(m2)
mm4= m1.add(m2)


"""function to elements/series(lists)"""
mm=m4.apply(lambda x:sum(x))
mm1=m4.applymap(lambda x:sum(x))
mm1=m4.applymap(lambda x:x**2)

l=[1,2,3,4]
print map(lambda x:x**2,l) # map syntax: r = map(func, seq)
print filter(lambda x:x**2<6,l) 

#def(x)=x**2
g=lambda x:x**2
print g(2)
