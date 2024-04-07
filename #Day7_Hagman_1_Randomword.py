import random
from MODULE_hangman_logo import *


hangman_word= ['green', 'apple', 'jasmin', 'camron', 'sweets']



# chosen_word=random.randint(0,len(hangman_word)-1)
# x=hangman_word[chosen_word]
# print(hangman_word[chosen_word])

word= random.choice(hangman_word)
print(word)

####version:1
# for x in word:
#     if x==guess_letter.lower():
#          print("MATCHED...")
#     else:
#          print("NOT Match :P")

####version:2
# guess=[]
# for x in word:
#      guess+='-'
# print(guess)

# guess_letter=input("Guess a letter..:?")

# for x in range(len(word)):
#     if word[x]==guess_letter.lower():
#          guess[x]=word[x]


guess=[]
length_word=len(word)
a=0

for x in word:
     guess+='-'
print(guess)


while a < length_word:
    guess_letter=input("Guess a letter..:?")
    for x in range(0,length_word):
        if word[x]==guess_letter.lower():
            guess[x]=word[x]
        else:
            print(stages[a])
    print(guess)
    a+=1

#cprint(guess)