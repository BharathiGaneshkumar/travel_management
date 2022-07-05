import datetime
import re
import time
#def booking():
        
def datechecker(l,fd=[]):
        l=l[:]
        if  datetime.date(l[-1],l[-2],l[0])<datetime.date.today():#time gap calculation must be included
                #print("Hi")
                return 0
        else:
                if len(fd)==0:
                        #print("Bye")
                        return 1
                else:
                        if datetime.date(fd[-1],fd[-2],fd[0])<datetime.date(l[-1],l[-2],l[0]):
                                return 1
                        else:
                                return -1
#def namechecker():
def uidcreator(n,a,d,idc,busdata):
        busdata=dict(busdata)
        x=str(datetime.datetime.now())
        date_of_booking="!".join(x.split())
        #print(date_of_booking)
        counter=format(idc,format("06d"))
        idc+=1
        uid=date_of_booking+"-"+counter      #
        datadictionary[uid]={"Name":n,"Age":a,"DateOfTravel":d,"Price":busdata["Price"]}
        return idc
        
def dotinput(firstdate=""):
        dot=input("Enter date of travel in dd/mm/yyyy format: ").strip()
        while dot[:2]=="00" or not(re.match(r"\d{2}/\d{2}/\d{4}",dot)):
                print("Invalid date format")
                dot=input("Enter date of travel in dd/mm/yyyy format: ").strip()
        dcomp=[int(x) for x in dot.strip().split("/")]
        is_valid_date=True
        try:
                datetime.datetime(dcomp[-1],dcomp[-2],dcomp[0]) 
        except ValueError:
                is_valid_date=False
        if(is_valid_date):
                if len(firstdate)==0:
                        if datechecker(dcomp):
                                date_of_travels.append(dot)
                        else:
                                print("The date has passed")
                                dotinput()
                else:
                        first=[int(y) for y in firstdate.split("/")]
                        temp=datechecker(dcomp,first)
                        if temp==-1:
                                print("Round trip date can't be less than first trip date")
                                dotinput(firstdate)
                        elif temp==1:
                                #print("correctdate")
                                date_of_travels.append(dot)
                        else:
                                print("The date has passed")
                                dotinput(firstdate)
                                
        else:
                print("Invalid Date")
                dotinput()
      #datadictionary[dot]={}
idcount=1
#Distance,Via,Type of bus Day
from_=input("Enter from: ")
to_=input("Enter To: ")
namelist=[]
agelist=[]
date_of_travels=[]
datadictionary={}
dotinput()
seats=int(input("Enter no of seats: ")) #seatlist must
busdata={}
currenttime=time.localtime(time.time())     #
currenthour=currenttime.tm_hour              #CURRENT TIME CALCULATION
currentmin=currenttime.tm_min                 #
correcttime=currenthour+(currentmin*0.01)
database={"karan":{"From":"Coimbatore","To":"Chennai","Distance":544,"Price":420,"timing":"22:20"},
          "mstravels":{"From":"Coimbatore","To":"Chennai","Distance":544,"Price":520,"timing":"18:20"},
          "sstravelz":{"From":"Coimbatore","To":"Chennai","Distance":544,"Price":420,"timing":"11:20"}}
travelz=database.keys()
for i in travelz:
        busscheduledtime=database[i]["timing"]    #
        scheduledtime=float(".".join(busscheduledtime.split(":")))
        today=time.localtime(time.time())
        todaylist=[str(today.tm_mday),str(today.tm_mon),str(today.tm_year)]
        for a in range(len(todaylist)-1):
                if len(todaylist[a])==1:
                        todaylist[a]="0"+todaylist[a]
        print(todaylist,date_of_travels[0].split("/"))
        if scheduledtime-correcttime>1 or date_of_travels[0].split("/")!=todaylist:
                busdata[i]=database[i]
for i in range(seats):
        t_name=input("Enter name: " )
        age=int(input("Enter age : "))
        namelist.append(t_name)
        agelist.append(age)
#type of buses,seats
trips=int(input("Enter 1 for round trip: ")) #implement as a tick option
#uidno=uidcreator()
#datadictionary[date_of_travels[0]]=uidno+"S"
if (trips==1):
        dotinput(date_of_travels[0])
        database1={"karan1":{"From":"Coimbatore","To":"Chennai","Distance":544,"Price":420,"timing":"22:20"},
          "mstravels1":{"From":"Coimbatore","To":"Chennai","Distance":544,"Price":520,"timing":"18:20"},
          "sstravelz1":{"From":"Coimbatore","To":"Chennai","Distance":544,"Price":420,"timing":"11:20"}}
        for q in database1.keys():
                busdata[q+"@"]=database1[q]
        #datadictionary[date_of_travels[-1]]=uidno+"R"
        #type of buses,seats
#print(namelist)
#print(agelist)
#print(date_of_travels)
print(busdata)
totalprice=0
#reqbus={"karan":{"From":"Coimbatore","To":"Chennai","Distance":544,"Price":420,"timing":"22:20"},
        #"karan1@":{"From":"Chennai","To":"Coimbatore","Distance":544,"Price":520,"timing":"22:20"}}
reqbus={"karan@":{"From":"Coimbatore","To":"Chennai","Distance":544,"Price":420,"timing":"22:20"}}
reqkeys=list(reqbus.keys())
if len(reqkeys)==2 and reqkeys[1][-1]!="@":
        reqkeys.insert(0,reqkeys.pop())     #karan karan@- i value  
for i in range(len(date_of_travels)):
        for j in range(len(namelist)):        #name age and seats - j value
                #print(idcount)
                if agelist[j]<=10 or agelist[j]>=60:
                        totalprice+=0.6*reqbus[reqkeys[i]]["Price"]
                else:
                        totalprice+=reqbus[reqkeys[i]]["Price"]
                idcount=uidcreator(namelist[j],agelist[j],date_of_travels[i],idcount,busdata[reqkeys[i]])
                time.sleep(0.002)
print(datadictionary,totalprice)       
 
        
        
        
