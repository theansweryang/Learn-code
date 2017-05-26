# -*- coding: utf-8 -*-
import datetime


"""get dates,change dates"""
d=datetime.date(2017,4,5)
print(d)
print(d.ctime())
print(d.isoweekday())

tdelta= datetime.timedelta(days=7)
tdelta2= d-datetime.date(2017,2,4)
print (tdelta2)
print (tdelta2.total_seconds())
print(d+tdelta)
print(d+2*tdelta)
print(d+tdelta2)


"""get time,change time"""
t=datetime.time(9,30,3,10000)
print t.hour

dt=datetime.datetime(2017,4,25,12,30,45)
print dt
print dt.time()

dtdelta= datetime.timedelta(days=7)
print dt+dtdelta

"""strftime format"""
dt_1=datetime.datetime.now()
print dt_1
print dt_1.strftime('%B-%d, %Y: %H')

dt_str='May-03, 2017: 15'
print datetime.datetime.strptime(dt_str,'%B-%d, %Y: %H')

"""pandas to_datatime"""
import pandas as pd
s = pd.Series(['3/11/2000', '3/12/2000', '3/13/2000']*3)
print s
s1=pd.to_datetime(s,format="%m/%d/%Y")
print s[0]-s[2]
print s1[0]-s1[2]