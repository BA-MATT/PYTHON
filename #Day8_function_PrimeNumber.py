
#user_input = int (input("Please enter the number to check is PRIME or not..:"))

def prime_number(user_input):
    if (user_input==2) or (user_input==3) or (user_input==5) or (user_input==7) or (user_input==11):
        print(f"Is PRIME Number : {user_input}")
    elif (user_input%2==0) or (user_input%3==0) or (user_input%5==0) or (user_input%7==0) or (user_input%11==0):
        print(f"Not PRIME Number : {user_input}")
    else:
        print(f"PRIME Number : {user_input}")

for x in range (1,100):
    prime_number(x)

