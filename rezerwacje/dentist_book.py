import datetime
list=[]
file= 'dentist.txt'
dentist_book={}
# dentist_book={date:list}
# list=[[numer][godzina]]
# data:list
#tworzenie tablicy godzin

#otwarta klinika: 9-17, godziny od 9 do 16
# hour=9
# while hour<17:
#     t= [0,hour]
#     list.append(t)
#     hour +=1
dates = [datetime.datetime.strptime('12/03/2023', '%m/%d/%Y')]
for date in dates:
    dentist_book[date] = [[0, hour] for hour in range(9, 17)]

def validate_number(number):
    if len(number) ==9 and number.isdigit():
        return True
    else: return False

def save_file(file):
    if check_availability_bool== True:
        with open(file, 'a') as file:
            for date, list in dentist_book.items():
                file.write(f"{date}: {list}\n")
                

def check_file_exist(file):
    try:
        with open(file, 'r'):
            pass
        return True
    except FileNotFoundError:
        print("Plik nie istnieje")
        return False

def get_appointments_from_file():
    with open('dentist.txt', "r") as file:
        file.read()
        
def check_availability_bool(time,date: datetime):
        if date in dentist_book.keys():
            if dentist_book[date][time-9][0]==0:
                return True
            else:return False
        else:return False

def check_availability(time,date: datetime):
        if check_availability_bool== True:
                return print("Dostępny termin")
        else: return print("termin wykorzystany")

def save_appointment(phone_number:str, time,date: datetime):
    if validate_number(phone_number) and check_availability_bool(time,date):
        print("błąd")
        return
    if date in dentist_book.keys():
        dentist_book[date][time - 9][0] = phone_number
    else:
        print("termin zajety")
    save_file(file)
    
        
def show_available_hours(date: datetime):
    if date in dentist_book:
        list= dentist_book[date]
        for i in range(8):
            if list[i][0]==0:
                print (list[i][1])

get_appointments_from_file()
save_appointment('987654321', 9, datetime.datetime.strptime('12/03/2023', '%m/%d/%Y'))
show_available_hours(datetime.datetime.strptime('12/03/2023', '%m/%d/%Y'))
save_file(file)