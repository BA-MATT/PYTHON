
user_input = int (input("Please enter the number to check is PRIME or not..:"))

def prime_number(user_input):
    if (user_input%2==0) or (user_input%3==0) or (user_input%5==0) or (user_input%7==0) or (user_input%11==0):
        print("Not PRIME Number")
    else:
        print("PRIME Number")

prime_number(user_input)

2