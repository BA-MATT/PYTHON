import math

test_h=int(input("please enter the height : "))
test_w=int(input("please enter the width : "))

coverage=5

def paint_can(height, width):
    cans=(height*width)/coverage
    number_of_cans=math.ceil(cans)
    print(f"You'll need {number_of_cans} cans of paints ")

paint_can(test_h,test_w)


