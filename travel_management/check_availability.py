import csv
import time
with open("E:\B.E CSE\Semester 2\Travel Management  Project\\finaldata.csv",'r') as f:
     r=csv.DictReader(f)
     while True:
          FROM=input("Enter From: ")#START LOCATION
          FROM=FROM.title()
          TO=input("Enter To: ")#END LOCATION
          TO=TO.title()
          index=0
          currenttime=time.localtime(time.time())     #
          currenthour=currenttime.tm_hour              #CURRENT TIME CALCULATION
          currentmin=currenttime.tm_min                 #
          correcttime=currenthour+(currentmin*0.01)#
          #correcttime=9.35
          print("Current Time",correcttime)
          data={}              #DICTIONARY WITH TIME AS KEY AND {BusNO:,ROUTES:,TRAVEL DURATION:} AS VALUE
          timelist=[]          #KEYSLIST OF DATA DICTIONARY
          xc=0
          pc=0
          for row in r:
               index+=1
               #print(row["BusNo"])
               #print(index)
               #print(row)
               routz=row["Routes"].split("|")  #ROUTES LIST
               tdiff=row["TD"].split()# TIME DIFFERENCE LIST-STRING VALUES
               try:
                    startindex=routz.index(FROM)
                    endindex=routz.index(TO)
               except ValueError:
                    #print("Hi")
                    continue
               #print(startindex,endindex)
               #print(routz)
               if  (startindex<endindex):
                    #tripslist=[]
                    #reqtime=20.45
                    tdiff=[int(x) for x in tdiff]       # TIME DIFFERENCE LIST-INTEGER VALUES
                    #print("Arrival place",routz[:startindex+1])
                    #print("original arrival list",tdiff)
                    #print("Arrival list",tdiff[:startindex+1])
                    temp1=sum(tdiff[:startindex+1])       
                    addhr1=temp1//60
                    addmin1=temp1%60
                    
                    #print(addtime)
                    reqtime=0   # APPROX ARRIVAL TIME OF BUS AT START
                    #print("trips: ",row["TT"].split())
                    #print(row["TT"].split())
                    for w in row["TT"].split():
                         hr=int(w[:w.index(":")])
                         if ("PM" in w and hr<12):
                              hr+=12
                         #print(w[w.index(":")+1:-2])
                         mi=int(w[w.index(":")+1:-2])
                         hr+=addhr1
                         mi+=addmin1
                         if (mi>=60):
                              mi-=60
                              hr+=1
                         result=hr+(mi*0.01)
                         if (result)>=correcttime:
                              #print("Selected Slot",w)
                              #print(hr,mi)
                              #print()
                              #reqtime=format(result,".2f")
                              reqtime=result
                              break
                         reqtime=0
                    if(reqtime==0):
                         #print("Bye")
                         continue
                    #print(reqtime)
                    if reqtime not in timelist:
                         timelist.append(reqtime)
                    
                    p=row["BusNo"]
                    q=routz[startindex:endindex+1]
                    #print(p,q)
                    #r=td
                    if reqtime not in data:
                         data[reqtime]={} 
                         data[reqtime]["BusNo"]=[]
                         data[reqtime]["Routes"]=[]
                         data[reqtime]["TravelDuration"]=[]
                    #data[reqtime]["BusNo"]=row["BusNo"]
                    #data[reqtime]["Routes"]=routz[startindex:endindex+1]

                    data[reqtime]["BusNo"].append(p)
                    data[reqtime]["Routes"].append(q)
                    #print(routz[startindex:endindex+1])
                    temp2=sum(tdiff[startindex:endindex+1])
                    #print("TRAVEL LIST",tdiff[startindex:endindex+1])
                    quo2=temp2//60
                    rem2=temp2%60
                    td=float(quo2)+(rem2*0.01)
                    #td=format(td,".2f")
                    #print(td)
                    data[reqtime]["TravelDuration"].append(td)#TRAVEL DURATION FROM START TO END
                    #data[reqtime]["TravelDuration"]=td
                    #print()
          #print("--------")          
          #print(data)
          
          #print(len(data),len(timelist))
          
          #for x in data:
            #   print(data[x]["BusNo"])
              # xc+=1
          #print(xc)
          #print("-----------------------------")
          #print(timelist)
          timelist.sort()
          #for p in timelist:
            #   print(data[x]["BusNo"])
           #    pc+=1
          #print(pc)
          #print(timelist)
          if (len(timelist)==0):
               print("No direct routes available")
          else:
               count=0
               if 0<len(timelist)<=4:
                    maxbusez=len(timelist)
               else:
                    maxbusez=4
               
               for timez in range(maxbusez):
                    clk=timelist[timez]
                    key=data[clk]
                    #print(key,clk)
                    #print(key["BusNo"])
                    for j in range(len(key["BusNo"])):
                         a=key["TravelDuration"][j]
                         #u=u*100
                         b=str(a)
                         temporary=b[b.index(".")+1:]
                         
                         #minut=float(temporary)*100
                         if len(temporary)==1:
                              temporary+='0'
                         #tradut=format(float(temporary),"f")
                         print("Bus No: {}".format(key["BusNo"][j]),"Estimated Arrival Time: {0:.2f}".format(clk),"Routes: {}".format(key["Routes"][j]),"Travel Duration: {0} hour {1} minutes".format(b[:b.index(".")],temporary),sep="\n")
                         print()
                         count+=1
                         if(count==maxbusez):
                              break
                    if(count==maxbusez):
                              break               
          break