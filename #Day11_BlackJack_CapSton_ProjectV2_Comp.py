import random
import math

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

player_score = []
comp_score= [] 

total_player=0 
total_comp=0 


def pick_card():
    """First run: To pull TWO random card from deck"""
    card_no=random.choices(cards,k=2)
    return card_no

def pick_sinlge_card():
    """Second Runt: To pull ONE random card from deck"""
    card_no=random.choice(cards)
    return card_no

player_score = pick_card()
comp_score = pick_card()

def addition(cards):
    # for x in score:
    #     sum_card+=x
    if sum(cards) == 21 and len(cards) ==2 :
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def addition_next(score):
    sum_card=0
    for x in score:
        sum_card+=x
    return sum_card

total_player=addition(player_score)
total_comp=addition(comp_score)

print (f"Computer card deck: {comp_score[0]}")
print (f"Computer {comp_score} card deck and total is : {total_comp}")
print (f"Player {player_score} card deck and total is : {total_player}")

cont_next = input ("Do you want to HIT of Stand: ").upper()

if cont_next=="H":
    while cont_next=="H":
        add_card=pick_sinlge_card()
        player_score.append(add_card)
        next_total_player=addition(player_score)
        if next_total_player>21:
                print ("BUST!!  YOU LOSE")
                break    

        if total_comp<17:
            add_card=pick_sinlge_card()
            comp_score.append(add_card)
            next_total_comp=addition(comp_score)

        print (f"{player_score} Player cards from deck and total is : {next_total_player}")
        print (f"{comp_score} Computer cards from deck ")
        
        cont_next = input ("Do you want to HIT of Stand: ").upper()
        if cont_next != "H":
            if next_total_player>21:
                print ("BUST!!  YOU LOSE")
                print (f"{player_score} card from deck and total is : {next_total_player}")
                print (f"{comp_score} card from deck and total is : {next_total_comp}")
                break
            elif next_total_comp>21:
                print ("BUST !! COMP LOSE")
                print (f"{player_score} card from deck and total is : {next_total_player}")
                print (f"{comp_score} card from deck and total is : {next_total_comp}")
                break
            elif next_total_comp == next_total_player:
                print ("Same score for Player and Computer")
                print (f"{player_score} card from deck and total is : {next_total_player}")
                print (f"{comp_score} card from deck and total is : {next_total_comp}")
                break
            elif next_total_comp > next_total_player:
                print ("COMPUTER wins.....")
                print (f"{player_score} card from deck and total is : {next_total_player}")
                print (f"{comp_score} card from deck and total is : {next_total_comp}")
                break
            else:
                print ("PLAYER wins.....")
                print (f"{player_score} card from deck and total is : {next_total_player}")
                print (f"{comp_score} card from deck and total is : {next_total_comp}")
                break


            



    
