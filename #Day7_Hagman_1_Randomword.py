import random
hangman_word= ['Green', 'Orange', 'Jasmin', 'Camron', 'David','Loyla','Kevin','Mel','Stuart']

chosen_word=random.randint(0,len(hangman_word)-1)
x=hangman_word[chosen_word]
print(hangman_word[chosen_word])


guess_letter=input("Please enter a word..?")
i=0
while i <= len(x):
    if guess_letter==x[i]:
        print("match")
    else:
         print("not match")
    i+=1
