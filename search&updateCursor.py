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
