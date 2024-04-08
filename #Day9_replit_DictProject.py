from replit import clear
from MODULE_Logo import logo

print(logo)
is_bid= True
bidder_record = {}

while is_bid is True:
    bid_name = input ("please enter bidder name: ")
    bid_amount = int(input ("please enter bidder amount: "))
    bidder_record.update({bid_name:bid_amount})

    bid = int(input ("Any else wanted to bid: "))
    if bid == 0:
        is_bid is False
        break
    else:
        is_bid is True
    clear()

"""Find Highesy bidder"""
def find_highest_bidder():
    hightest_amnt=0
    winner=""
    for bidder in bidder_record:
        amount=bidder_record[bidder]
        if amount > hightest_amnt:
            hightest_amnt=amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${hightest_amnt}")


print(bidder_record)
find_highest_bidder()
