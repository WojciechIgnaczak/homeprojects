#phone book= [username,number]
phone_book=[]
file= "book.txt"
def validate_number(number :str)->bool:
    if len(number) ==9 and number.isdigit():
        return True
    else: return False

def read_phonebook():
    with open('book.txt', 'r') as file:
       return file.read()

def save_phonebook(phone_book):
    with open('book.txt', 'w') as file:
            for i in phone_book:
                file.write(f"{i}\n")

def display_phonebook():
        print(phone_book)

def add_entry(name:str,number:str):
    if validate_number(number):
        t=[name,number]
        phone_book.append(t)
        return phone_book

def modify_entry(old_number:str,new_number:str,new_name:str):
    if validate_number(new_number):   
        for i in phone_book:
            if i[1] == old_number:
                i[1] = new_name
                i[0] = new_number
            else: print("taki numer nie istnieje")
        return phone_book
    else: print("bledny nowy numer telefony")

def delete(number :str):
    for i  in phone_book:
        if i[1] == number:
            phone_book.remove(i)
    return phone_book
read_phonebook()
add_entry("wojtek","123456789")
add_entry("wotek","123456489")
display_phonebook()
save_phonebook(phone_book)