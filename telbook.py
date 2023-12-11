file_path='telbook.txt'

def validate_number(number):
    if number.isdigit() and len(number)==9 :
        return True
    else:
        print("zly numer")
        return False
    
def number_exist(number):
    book=read()
    for i in book:
        if len(i)>0 and i[1]==number:
            print("numer istnieje")
            return False
    return True

def read():
    book=[]
    try:
        with open(file_path,'r') as file:
            for line in file:
                numer=line.strip().split(';')
                book.append(numer)
    except:
        book=[]
    return book

def save(name,number):
    if validate_number(number)==True and number_exist(number)==True:
        with open(file_path,'a')as file:
            file.write(f"{name} ;{number}\n")
            print("zapisano")

def display():
    with open(file_path,'r') as file:
        print(file.read())

def delete(number):
    book=read()
    new_book=[]
    for i in book:
        if not i[1]==number:
            new_book.append(i)
    with open(file_path,'w')as file:
        for j in new_book:
            file.write(f"{j[0]};{j[1]}\n")

def modify_entry(old_phone_number, new_name, new_phone_number):
    book=read()
    for i in book:
        if i[1]==old_phone_number:
            i[0]=new_name
            i[1]=new_phone_number
        with open(file_path,'w')as file:
            file.write(f"{i[0]};{i[1]}\n")
        print("zmodyfikowano")
#save('user4','123456789')
delete("123456789")