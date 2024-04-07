list1=["A1","A2","A3"]
list2=["B1","B2","B3"]
list3=["C1","C2","C3"]

map=[list1,list2,list3]

print("Hiding your treasure! X marks the spot.")
position = input()
letter = position[0].lower()
abc=["a","b","c"]

letter_index=abc.index(letter)
number_index=int(position[1])-1

map[number_index][letter_index]="X"

print(f"{list1}\n{list2}\n{list3}")