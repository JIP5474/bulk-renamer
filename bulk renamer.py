import os
import re
files = os.listdir()
path=os.getcwd()
sub=input("Enter sub:")
def new_name(filename):
        s=0
        month_name=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        for i in filename:
                if i == '-':
                        break
                else:
                        s+=1
        s=s+6
        end=s+1
        month=filename[s:end:1]
        month=int(month);
        month=month_name[month-1]
        s=s+1
        end=s+2
        date=filename[s:end:1]
        new_n=sub+" "+month+date
        return new_n
for f in files:
        if "Meeting Recording" in f:
                oldname=path+'\\'+f
                name=path+'\\'+new_name(f)+".mp4"
                os.rename(oldname,name)
