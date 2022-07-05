from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as login_auth
from home.models import Availability_from_and_to,Contact,Bus,Book
from django.contrib import messages
from decimal import Decimal
from django.contrib.auth.decorators import login_required
import csv
import time

def home(request):
    return render(request,'home.html')

def availability(request):
    if request.method == "POST":
        availability.FROM = request.POST.get('FROM')
        availability.TO = request.POST.get('TO')
        a=Availability_from_and_to(FROM = availability.FROM,TO = availability.TO)
        a.save()
        return redirect('/availabilitydisplay')
    return render(request,'availability.html')

def register(request):
     form = UserCreationForm
     if request.method == "POST":
          regForm = UserCreationForm(request.POST)
          if regForm.is_valid():
               regForm.save()
               messages.success(request,"User has been registered.")
     return render(request,'registration/register.html',{'form':form})

def faq(request):
    return render(request,'faq.html')

def availabilitydisplay(request):
    with open("finaldata.csv",'r') as f:
        r=csv.DictReader(f)
        while True:
          BUS_NUMBER = ['-','-','-','-']
          ESTIMATED_ARRIVAL_TIME = ['-','-','-','-']
          ROUTES = ['-','-','-','-']
          ESTIMATED_DURATION= ['-','-','-','-']
          FROM=availability.FROM.title()
          TO=availability.TO.title()
          currenttime=time.localtime(time.time())    
          currenthour=currenttime.tm_hour              
          currentmin=currenttime.tm_min                 
          correcttime=currenthour+(currentmin*0.01)
          data={}              
          timelist=[]          
          for row in r:
               routz=row["Routes"].split("|")  
               tdiff=row["TD"].split()
               try:
                    startindex=routz.index(FROM)
                    endindex=routz.index(TO)
               except ValueError:  
                    continue
               if  (startindex<endindex):
                    tdiff=[int(x) for x in tdiff]      
                    temp1=sum(tdiff[:startindex+1])       
                    addhr1=temp1//60
                    addmin1=temp1%60
                    reqtime=0   
                    for w in row["TT"].split():
                         hr=int(w[:w.index(":")])
                         if ("PM" in w and hr<12):
                              hr+=12
                         mi=int(w[w.index(":")+1:-2])
                         hr+=addhr1
                         mi+=addmin1
                         if (mi>=60):
                              mi-=60
                              hr+=1
                         result=hr+(mi*0.01)
                         if (result)>=correcttime:
                              reqtime=result
                              break
                         reqtime=0
                    if(reqtime==0): 
                         continue
                    if reqtime not in timelist:
                         timelist.append(reqtime)
                    p=row["BusNo"]
                    q=routz[startindex:endindex+1]
                    if reqtime not in data:
                         data[reqtime]={} 
                         data[reqtime]["BusNo"]=[]
                         data[reqtime]["Routes"]=[]
                         data[reqtime]["TravelDuration"]=[]
                    data[reqtime]["BusNo"].append(p)
                    data[reqtime]["Routes"].append(q)
                    temp2=sum(tdiff[startindex:endindex+1])
                    quo2=temp2//60
                    rem2=temp2%60
                    td=float(quo2)+(rem2*0.01)
                    data[reqtime]["TravelDuration"].append(td)
          timelist.sort()
          if (len(timelist)==0):
               return render(request,"noroutes.html",{'error':'No direct routes available'})
          else:
               count=0
               if 0<len(timelist)<=4:
                    maxbusez=len(timelist)
               else:
                    maxbusez=4
               for timez in range(maxbusez):
                    clk=timelist[timez]
                    key=data[clk]    
                    for j in range(len(key["BusNo"])):
                         a=key["TravelDuration"][j] 
                         b=str(a)
                         temporary=b[b.index(".")+1:]
                         if len(temporary)==1:
                              temporary+='0'
                         BUS_NUMBER[count]=key["BusNo"][j]
                         ESTIMATED_ARRIVAL_TIME[count]="{0:.2f}".format(clk)
                         ROUTES[count]=key["Routes"][j]
                         ESTIMATED_DURATION[count]="{0} hour {1} minutes".format(b[:b.index(".")],temporary)
                         count+=1
                         if(count==maxbusez):
                              break
                    if(count==maxbusez):
                              break
               return render(request,"availabilitydisplay.html",{'BUS_NO_1':BUS_NUMBER[0],'BUS_NO_2':BUS_NUMBER[1],'BUS_NO_3':BUS_NUMBER[2],'BUS_NO_4':BUS_NUMBER[3],'ESTIMATED_ARRIVAL_TIME_1':ESTIMATED_ARRIVAL_TIME[0],'ESTIMATED_ARRIVAL_TIME_2':ESTIMATED_ARRIVAL_TIME[1],'ESTIMATED_ARRIVAL_TIME_3':ESTIMATED_ARRIVAL_TIME[2],'ESTIMATED_ARRIVAL_TIME_4':ESTIMATED_ARRIVAL_TIME[3],'ESTIMATED_DURATION_1':ESTIMATED_DURATION[0],'ESTIMATED_DURATION_2':ESTIMATED_DURATION[1],'ESTIMATED_DURATION_3':ESTIMATED_DURATION[2],'ESTIMATED_DURATION_4':ESTIMATED_DURATION[3]})               
          
def noroutes(request):
     return render(request,"noroutes.html")

def routes(request):
     with open("finaldata.csv",'r') as f:
        r=csv.DictReader(f)
        while True:
          BUS_NUMBER = ['-','-','-','-']
          ESTIMATED_ARRIVAL_TIME = ['-','-','-','-']
          ROUTES = ['-','-','-','-']
          ESTIMATED_DURATION= ['-','-','-','-']
          FROM=availability.FROM.title()
          TO=availability.TO.title()
          currenttime=time.localtime(time.time())    
          currenthour=currenttime.tm_hour              
          currentmin=currenttime.tm_min                 
          correcttime=currenthour+(currentmin*0.01)
          data={}              
          timelist=[]          
          for row in r:
               routz=row["Routes"].split("|")  
               tdiff=row["TD"].split()
               try:
                    startindex=routz.index(FROM)
                    endindex=routz.index(TO)
               except ValueError:  
                    continue
               if  (startindex<endindex):
                    tdiff=[int(x) for x in tdiff]      
                    temp1=sum(tdiff[:startindex+1])       
                    addhr1=temp1//60
                    addmin1=temp1%60
                    reqtime=0   
                    for w in row["TT"].split():
                         hr=int(w[:w.index(":")])
                         if ("PM" in w and hr<12):
                              hr+=12
                         mi=int(w[w.index(":")+1:-2])
                         hr+=addhr1
                         mi+=addmin1
                         if (mi>=60):
                              mi-=60
                              hr+=1
                         result=hr+(mi*0.01)
                         if (result)>=correcttime:
                              reqtime=result
                              break
                         reqtime=0
                    if(reqtime==0): 
                         continue
                    if reqtime not in timelist:
                         timelist.append(reqtime)
                    p=row["BusNo"]
                    q=routz[startindex:endindex+1]
                    if reqtime not in data:
                         data[reqtime]={} 
                         data[reqtime]["BusNo"]=[]
                         data[reqtime]["Routes"]=[]
                         data[reqtime]["TravelDuration"]=[]
                    data[reqtime]["BusNo"].append(p)
                    data[reqtime]["Routes"].append(q)
                    temp2=sum(tdiff[startindex:endindex+1])
                    quo2=temp2//60
                    rem2=temp2%60
                    td=float(quo2)+(rem2*0.01)
                    data[reqtime]["TravelDuration"].append(td)
          timelist.sort()
          if (len(timelist)==0):
               return render(request,"noroutes.html",{'error':'No direct routes available'})
          else:
               count=0
               if 0<len(timelist)<=4:
                    maxbusez=len(timelist)
               else:
                    maxbusez=4
               for timez in range(maxbusez):
                    clk=timelist[timez]
                    key=data[clk]    
                    for j in range(len(key["BusNo"])):
                         a=key["TravelDuration"][j] 
                         b=str(a)
                         temporary=b[b.index(".")+1:]
                         if len(temporary)==1:
                              temporary+='0'
                         BUS_NUMBER[count]=key["BusNo"][j]
                         ESTIMATED_ARRIVAL_TIME[count]="{0:.2f}".format(clk)
                         ROUTES[count]="-".join(key["Routes"][j])
                         ESTIMATED_DURATION[count]="{0} hour {1} minutes".format(b[:b.index(".")],temporary)
                         count+=1
                         if(count==maxbusez):
                              break
                    if(count==maxbusez):
                              break
               return render(request,"routes.html",{'BUS_NO_1':BUS_NUMBER[0],'BUS_NO_2':BUS_NUMBER[1],'BUS_NO_3':BUS_NUMBER[2],'BUS_NO_4':BUS_NUMBER[3],'ESTIMATED_ARRIVAL_TIME_1':ESTIMATED_ARRIVAL_TIME[0],'ESTIMATED_ARRIVAL_TIME_2':ESTIMATED_ARRIVAL_TIME[1],'ESTIMATED_ARRIVAL_TIME_3':ESTIMATED_ARRIVAL_TIME[2],'ESTIMATED_ARRIVAL_TIME_4':ESTIMATED_ARRIVAL_TIME[3],'ROUTE_1':ROUTES[0],'ROUTE_2':ROUTES[1],'ROUTE_3':ROUTES[2],'ROUTE_4':ROUTES[3],'ESTIMATED_DURATION_1':ESTIMATED_DURATION[0],'ESTIMATED_DURATION_2':ESTIMATED_DURATION[1],'ESTIMATED_DURATION_3':ESTIMATED_DURATION[2],'ESTIMATED_DURATION_4':ESTIMATED_DURATION[3]})               

def contact(request):
     if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact= Contact(name = name, phone = phone, desc = desc)
        contact.save()
     return render(request,'contact.html')


@login_required(login_url='login')
def findbus(request):
    context = {}
    if request.method == 'POST':
        source_r = request.POST.get('source')
        dest_r = request.POST.get('destination')
        date_r = request.POST.get('date')
        bus_list = Bus.objects.filter(source=source_r, dest=dest_r, date=date_r)
        if bus_list:
            return render(request, 'list.html', locals())
        else:
            context["error"] = "Sorry no buses availiable"
            return render(request, 'findbus.html', context)
    else:
        return render(request, 'findbus.html')

@login_required(login_url='login')
def bookings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('bus_id')
        seats_r = int(request.POST.get('no_seats'))
        bus = Bus.objects.get(id=id_r)
        if bus:
            if bus.rem > int(seats_r):
                name_r = bus.bus_name
                cost = int(seats_r) * bus.price
                source_r = bus.source
                dest_r = bus.dest
                nos_r = Decimal(bus.nos)
                price_r = bus.price
                date_r = bus.date
                time_r = bus.time
                username_r = request.user.username
                userid_r = request.user.id
                rem_r = bus.rem - seats_r
                Bus.objects.filter(id=id_r).update(rem=rem_r)
                book = Book.objects.create(name=username_r, userid=userid_r, bus_name=name_r,
                                           source=source_r, busid=id_r,
                                           dest=dest_r, price=price_r, nos=seats_r, date=date_r, time=time_r,
                                           status='BOOKED')
                # book.save()
                return render(request, 'modal.html', {'bus_name':name_r,'source':source_r,'dest':dest_r,'nos':seats_r,'price':price_r,'cost':cost,'date':date_r,'time':time_r})
            else:
                context["error"] = "Sorry select fewer number of seats"
                return render(request, 'findbus.html', context)

    else:
        return render(request, 'findbus.html')

@login_required(login_url='login')
def cancellings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('bus_id')
        #seats_r = int(request.POST.get('no_seats'))

        try:
            book = Book.objects.get(id=id_r)
            bus = Bus.objects.get(id=book.busid)
            rem_r = bus.rem + book.nos
            Bus.objects.filter(id=book.busid).update(rem=rem_r)
            #nos_r = book.nos - seats_r
            Book.objects.filter(id=id_r).update(status='CANCELLED')
            Book.objects.filter(id=id_r).update(nos=0)
            return redirect(seebookings)
        except Book.DoesNotExist:
            context["error"] = "Sorry You have not booked that bus"
            return render(request, 'error.html', context)
    else:
        return render(request, 'findbus.html')

@login_required(login_url='login')
def seebookings(request,new={}):
    context = {}
    id_r = request.user.id
    book_list = Book.objects.filter(userid=id_r)
    if book_list:
        return render(request, 'booklist.html', locals())
    else:
        context["error"] = "Sorry no buses booked"
        return render(request, 'findbus.html', context)

def success(request):
    context = {}
    context['user'] = request.user
    return render(request, 'success.html', context)

def modal(request):
     return render(request, 'modal.html')