'''program ktory w pliku przechpwuje klocki i ich rodzaj'''
import json

file_path='klocki1.json'

def odczyt():
    try:    
        with open(file_path,'r') as file:
            dane= json.load(file)
    except:
        dane={}
    return dane

def validate_ilosc(ilosc):
    if ilosc.isdigit() and int(ilosc)>=0:
        return True
    else: return False

def zapis_do_pliku(rodzaj,ilosc):
    data=odczyt()
    if not rodzaj in data.keys():
        if not validate_ilosc(ilosc):
            print("zla ilosc")
            return False
        new_dane={rodzaj:ilosc}
        data.update(new_dane)
        with open(file_path,'w') as file:
            json.dump(data,file)
        print("zapisono do pliku")
    else: print("dany rodzaj istnieje")
def delete(rodzaj):
    type= odczyt()
    if rodzaj in type.keys():
        del type[rodzaj]
        with open(file_path,'w') as file:
            json.dump(type,file)
        print("usunieto")
    else:
        print("brak danego rodzaju klocków do usuniecia")

def modify_ilosc(rodzaj,new_ilosc):
    type= odczyt()
    if rodzaj in type.keys():
        type[rodzaj]=new_ilosc
        with open(file_path,'w') as file:
            json.dump(type,file)
        print('zmodyfikowano rodzaj')
    else:
        print("brak danego rodzaju do modyfikowania")
def display():
    slownik= odczyt()
    print(slownik)
########################################################################################################################################
#WYKONYWANIE PROGRAMU
wybor = True
while wybor==True:
    print("co chesz zrobic? Wybierz odpowiedni numer 1.Dodaj rodzaj i ilosc, 2.Usun po rodzaju, 3.Zmodyfikuj ilosc,4.Wyjdź")
    display()
    co_robic= input("podaj instrukcje: ")
    if co_robic =='1':
        rodzaj =input("Podaj rodzaj klocka: ")
        ilosc=input("Podaj ilosc: ")
        zapis_do_pliku(rodzaj,ilosc)
    elif co_robic=='2':
        rodzaj =input("Podaj rodzaj klocka: ")
        delete(rodzaj)
    elif co_robic=='3':
        rodzaj =input("Podaj rodzaj klocka: ")
        ilosc=input("Podaj nowa ilosc: ")
        modify_ilosc(rodzaj,ilosc)
    elif co_robic=='4':
        wybor=False
    else: wybor=False