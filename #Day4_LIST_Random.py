import random

names = ['Sam', 'Pam', 'Jas', 'Max', 'David','Loyla','Kevin','Mel','Stuart']

len_list = len(names);

Turn =  random.randint(0,len_list)

print(f"{names[Turn]} is going to buy the meal today")