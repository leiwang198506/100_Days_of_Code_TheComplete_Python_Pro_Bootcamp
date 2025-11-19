# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


import art
print(art.logo)
bid_info={}
name=input("What is your name?\n")
price=int(input("What is your bid?\n"))
bid_info[name]=price
loop_option=input("Are there any other bidders? Type 'yes ' or 'no'\n")
continue_bid = True
while continue_bid:
    if loop_option=="yes":
        print("\n" * 100)
        name = input("What is your name?\n")
        price = int(input("What is your bid?\n"))
        bid_info[name] = price
        loop_option = input("Are there any other bidders? Type 'yes ' or 'no'\n")
    else:
        continue_bid = False
winner_bid=0
for name, price in bid_info.items():
    if price> winner_bid:
        winner_bid= price

revised_bid_info= {v:k for k,v in bid_info.items()}
winner_name=revised_bid_info[winner_bid]


print(f"The winner is {winner_name} with a bid of {winner_bid}")






