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


-------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------
##only use da. class to search and update.. 
#a_code_to_read_attribute_table
fields=[ i.name for i in arcpy.ListFields('lc2011_LC')]#get all the fields,记住要加上name
srCursor= arcpy.da.SearchCursor('lc2011_LC',fields)#建立一个SEARCH cursor
for row in srCursor:
    print (row) #each row is a tuple
del srchcur 

#a_code_to_update_attribute_table
updateCursor= arcpy.da.UpdateCursor('lc2011_LC',fields)#建立一个SEARCH cursor
for row in updateCursor:
    print (row)#each row is a list
del updateCursor 

updateCursor= arcpy.da.UpdateCursor('lc2011_LC',fields)#建立一个SEARCH cursor
for row in updateCursor:
    row[-1]=row[0] #here you can make changes
    updateCursor.updateRow(row)#don't forget to updateRow
del updateCursor 

