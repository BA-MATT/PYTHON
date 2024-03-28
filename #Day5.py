sum_even2=0
# Sum of Even number method 2
for Number in range(1,31):
    if Number%3==0 and Number%5==0  :
        print("FizzBuzz")
    elif Number%3==0:
        print("Fizz")
    elif Number%5==0:
        print("Buzz")
    else:
        print(Number)