import os

path=os.getcwd()        #saving path to the file
file=os.listdir()       #listing directories

#getting common name to be included from user
common=input("Enter common name to be included:")  

#function for getting the new name
def new(filename):
    index=0

    #month list for reference
    month_list=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    #for loop for searching the filename for specific char
    for i in filename:
        if i=='-':      #if char found break
            break
        else:           #else increase index
            index+=1
    #index is set to the position for grabbing month        
    index=index+5
    end=index+2
    month=int(filename[index:end:1])    #string slicing to get month
    month=month_list[month-1]    #comparing with the month list to get monthname

    #index is set for grabbing date
    index=index+2
    end=index+2
    date=filename[index:end:1]      #string slicing to get date
    new_n=common+" "+month+date    #concatening all into new name
    return new_n


#for loop for each filename
for f in file:
    if "Meeting Recording" in f:        #if matching file found
        oldname=path+'\\'+f             #oldname is set    
        newname=path+'\\'+new(f)+".mp4" #newname is set with return value from function
        os.rename(oldname,newname)      #renaming the file
        
