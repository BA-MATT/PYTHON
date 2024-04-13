from MODULE_CalcLogo import logo

#addition
def add(n1,n2):
    return n1+n2

#Substract
def substract(n1,n2):
    return n1-n2

#multiply
def multiply(n1,n2):
    return n1*n2

#divide'
def divide(n1,n2):
    return n1/n2

operations = { 
    "+": add,
    "-": substract, 
    "*": multiply, 
    "/": divide 
    }

print(logo)

"""First Time run"""
num1= int(input("Please enter the value of n1 : "))

"""display key of Dictionary"""
for symbol in operations:
    print(symbol)

operation_symbol = input ("Pick an operation from line above: ")

num2= int(input("Please enter the value of n2 : "))

calculation_function = operations[operation_symbol]
answer=calculation_function(num1,num2)
print (f"{num1}  { operation_symbol} {num2} = {answer}")

"""Second and N Time run"""
calc_continue= input("Do you still wanted to continue press Y or N : ").lower()
final_answer=answer

if calc_continue=='y':
    while calc_continue=='y':
        """display key of Dictionary"""
        for symbol in operations:
             print(symbol)
        
        operation_symbol = input ("Pick an operation from line above: ")
        num3= int(input("Please enter the NEXT value : "))

        calculation_function = operations[operation_symbol]
        answer2=calculation_function(final_answer,num3)
        

        print (f"{final_answer}  { operation_symbol} {num3} = {answer2}")

        calc_continue= input("Do you still wanted to continue press Y or N : ").lower()
        if calc_continue=='n':
            break
        else:
            final_answer=answer2








