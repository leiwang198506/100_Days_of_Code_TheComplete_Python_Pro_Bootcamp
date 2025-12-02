cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#get your cards in a list
if_play=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if if_play=="y":
    import random
    #Deal both user and computer a starting hand of 2 random card values.
    computer_cards = random.sample(cards, k=2)
    print(computer_cards)
    player_cards = random.sample(cards, k=2)
    print(player_cards)
#Detect when computer or user has a blackjack. (Ace + 10 value card).
#If computer gets blackjack, then the user loses
# (even if the user also has a blackjack). If the user gets a blackjack,
# then they win (unless the computer also has a blackjack).
    if sorted(computer_cards) ==sorted([11,10]):
        print("Computer win, You lose!")
    elif sorted(player_cards) ==sorted([11,10]):
        print("You win!")
#Calculate the user's and computer's scores based on their card values.
    current_computer_score = computer_cards[0] + computer_cards[1]
    if 11 in computer_cards:
        if current_computer_score > 21:
           index = computer_cards.index(11)
           computer_cards[index]=1
    print(f"Computer's first card: {computer_cards[0]}")


    current_player_score= player_cards[0]+player_cards[1]



else:
    print("Go away!")

    #
    # computer_first_card = computer_cards[0]
    #
    # # calculate current score
    #
    #
    #
    # #generate computer's card
    #
    #
    # if current_computer_score == 21:
    #     print("You lose!")
    # else:
    #     current_player_score == 21
    #     print("You win!")
    #
    # #print out all instructions
    # print(f"Your cards: {player_cards}, current score: {current_score}\n"
    #       f"Computer's first card: {computer_first_card}")
    # #choice
    # choice=input("Type 'y' to get another card, type 'n' to pass: \n")
    # if choice=="y":
    #     player_cards.append(random.sample(cards,1)[0])
    #     current_score = player_cards[0] + player_cards[1]+ player_cards[2]
    #     print(f"Your cards: {player_cards}, current score: {current_score}\n"
    #           f"Computer's first card: {computer_first_card}")
    #
