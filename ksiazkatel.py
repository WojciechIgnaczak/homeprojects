'''napisz wizyty u dentysty:
data:godzina,numer telefonu,nazwa'''

import json
import datetime
file_path= 'visit.json'

def validate_number_exist(number:str):
    visit= read()
    if number.isdigit() and len(number)==9:
       return True
    else:
        print("zly numer")
        return False
    
def validate_date(date:datetime):
    visit=read()
    data= datetime.datetime.strptime(date,"%Y-%m-%d %H:00")  
    if not data in visit.keys():
        if data.strftime('%Y-%m-%d'):
         return True
    else:
        print('zla data')
        return False
def check_ilosc(date:datetime):
    visit=read()
    #data=datetime.datetime.strftime(date,"%Y-%m-%d")
    daty=list(visit.keys())
    counter=0
    for d in daty:
        daata=d.split(" ")
        if date ==d:
            counter+=1
    if counter>=8:
        print("wszystko zajete")
        return False
    return True
 
def check_available_hour(date):
    visit= read()
    wartosci=list(visit.keys())
    dlugosc=len(wartosci)
    for i in range (dlugosc):
        if wartosci[i]==date:
            print("Godzina zajęta")
            return False
    print('godzina wolna')
    return True  

def read():
    try:
        with open(file_path,'r') as file:
            visit=json.load(file)
    except:
        visit={}
    return visit

def new_visit(date:datetime,number:str,user:str):
    if validate_date(date) and validate_number_exist(number) and check_available_hour(date) and check_ilosc(date):
        visit=read()
        new={date:[number,user]}
        visit.update(new)
        with open(file_path,'w') as file:
            json.dump(visit,file)


def display():
    slownik=read()
    print(slownik)
    



#new_visit('2023-02-12 17:00','123456789','user')
#display()
#check_available_hour("2022-02-12 19:00")
#check_ilosc('2023-02-12 7:00')