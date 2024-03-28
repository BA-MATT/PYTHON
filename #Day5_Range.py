sum_even1=0
# Sum of Even number method 1
for evens in range(1,100):
    if evens%2==0:
        sum_even1+=evens

sum_even2=0
# Sum of Even number method 2
for evens1 in range(0,100,2):
    sum_even2+=evens1
        
print (sum_even1)
print (sum_even2)