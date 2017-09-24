# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import arcpy
import pandas as pd

##first step always for set up workspace, env can do all on environment settings
workspace=r"C:\EsriTraining\py_scripting_geoprocessing\py_scripting_geoprocessing.gdb"
arcpy.env.workspace = workspace #remember to add r, so \ don't count

arcpy.env.overwriteOutput = True  ##overwrite important for working arcpy, play with parameters


##points data to a feature layer
arcpy.CreateFeatureclass_management(workspace,'ptslist2',geometry_type="POINT",spatial_reference="attr_with_rank")

##add fields to the table
arcpy.AddField_management('ptslist2','name','text')

##create cursor object and add value to a table, 记住用da.
editcursor=arcpy.da.InsertCursor("ptslist2",['SHAPE@XY','name']) 
ab=[107.8173305, -37.4966125]
#row=(ab,'yang')#注意必须是这种tuple嵌套的形式
editcursor.insertRow([ab,'heating'])
del editcursor#del很重要，del之后data才不会lock


##search cursor to extract field values
#sometimes data layers goes bad, you need to export to another name and delete previous one.
srchcur= arcpy.SearchCursor('Roads') #a searchcursor class, 这里没有用da.,用的原来的老function
for row in srchcur:
    print(row.getValue('SHAPE_Length'))#makesure the name is full name not alias name of the field 

del srchcur  

## Caculate the field using python
codeblock="""def gettype(ROUTE_TYPE,ROUTE_NUMBER):
    if int(ROUTE_NUMBER)>300 and ROUTE_TYPE=='Light_duty':
        return 3333""" #code block is the py function 
    
expression='gettype(!ROUTE_TYPE!,!ROUTE_NUMBER!)' #use !! sign to get field values
arcpy.CalculateField_management('Roads','DISTANCE',expression,"PYTHON_9.3",codeblock)

##update cursor to delete certain features
cursor=arcpy.UpdateCursor('Invasive_plants') #a searchcursor class, 这里没有用da.,用的原来的老function
for row in cursor:
    if (row.getValue('MAP_ID'))<5:
        cursor.deleteRow(row)
del cursor




