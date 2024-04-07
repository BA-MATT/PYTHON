import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



def generator(nr):
    password = " "
    for x in range(0,nr):
        p=random.randint(0,len(letters)-1)
        #print(letters[p])
        password+=letters[p]
    return password
    #print(password)

def generator1(nr):
    password = " "
    for x in range(0,nr):
        p=random.randint(0,len(numbers)-1)
        #print(numbers[p])
        password+=numbers[p]
    return password

def generator2(nr):
    password = " "
    for x in range(0,nr):
        p=random.randint(0,len(symbols)-1)
        #3print(symbols[p])
        password+=symbols[p]
    return password

letter=generator(nr_letters) 
symbol=generator1(nr_symbols) 
num=generator2(nr_numbers) 


def remove(string):
    return string.replace(" ","")

string=letter+symbol+num

print(string)

print(remove(string))





