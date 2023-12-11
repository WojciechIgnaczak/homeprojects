#otwarte 9-17,co godzina wizyta
#data;godzina;numer
import datetime
import os
file_path='resdent2.txt'

    
def validate_number(number):
    if number.isdigit() and len(number)==9:
        return True
    else:
        print("zly numer")
        return False

def validate_date(date:datetime):
    try:
        data=datetime.datetime.strptime(date,"%Y-%m-%d") 
        return True
    except:
        print("zly format daty yyy-mm-dd")
        return False
    
def validate_hour(hour):
    try:
        hours=datetime.datetime.strptime(hour,"%H:00") 
        if hours.hour in range(9,17):
            return True
    except:
        print("zla godzina, zly format godziny HH:00")
        return False
    
def czy_godzina_zajeta(date,hour):
    visit=read(file_path)
    for i in visit:
        if i[0]==date:
            if i[1]==hour:
                print("godzina zajeta")
                return False
    else:
        return True
    
def zlicz_godziny(date:datetime):
        visit=read(file_path)
        counter=0
        for i in visit:
            if i[0]==str(date):
                counter= counter +1
        if counter<8:
            return True
        else:
            print("wszystkie godziny zajete")
            return False
        
def validate_all(date,number,hour):
    if validate_date(date)==True and validate_hour(hour)==True  and validate_number(number)==True and czy_godzina_zajeta(date,hour)==True and zlicz_godziny(date)==True :
        return True
    else: return False

def check_file_exist(file_path):
    return os.path.exists(file_path)

def read(file_path):
    app=[]
    try:
        check_file_exist(file_path)
        with open(file_path,'r') as file:
            for line in file:
                wizyta=line.strip().split(';')
                app.append(wizyta) 
    except:
        app=[]
    return app

def save_visit(date,hour,number):
    if validate_all(date,number,hour):
        visit=read(file_path)
        with open(file_path,'a') as file:
            file.write(f"{date};{hour};{number}\n")

def display():
    visit=read(file_path)
    print(visit)

def display_available_hours(date):
    working_hour=[]
    for i in range (9,17):
        working_hour.append(f"{i}:00")

    booked_hours=[]
    visit=read(file_path)
    for j in visit:
        if j[0]==date:
            booked_hours.append(j[1])

    free_hours= working_hour
    for working_hour in booked_hours:
        free_hours.remove(working_hour)
    print(free_hours)

save_visit('2023-12-12','9:00','123456789')