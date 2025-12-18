cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#task checklist: https://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#get your cards in a list
if_play=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if if_play=="y":
    import random
#task 1: Deal both user and computer a starting hand of 2 random card values.
    computer_cards = random.sample(cards, k=2)
    print(computer_cards)
    player_cards = random.sample(cards, k=2)
    current_computer_score = sum(computer_cards)
    current_player_score = sum(player_cards)
    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}\n"
                       f"Computer's first card: {computer_cards[0]}")
    def play_card():
        user_continue_draw = True
        while user_continue_draw:
        #task 2: Detect when computer or user has a blackjack. (Ace + 10 value card).
        #task 3: If computer gets blackjack, then the user loses
        # (even if the user also has a blackjack). If the user gets a blackjack,
        # then they win (unless the computer also has a blackjack).
                # task 4: Calculate the user's and computer's scores based on their card values.

            if sorted(player_cards) == sorted([11, 10]):
                user_continue_draw = False
                print("You win!")
            elif sorted(computer_cards) ==sorted([11,10]):
                user_continue_draw= False
                print("Computer win, You lose!")
            else:
                if current_player_score > 21:
                    if 11 in player_cards:
                        index = player_cards.index(11)
                        player_cards[index]=1
                        if current_player_score > 21:
                            user_continue_draw = False
                            print("Computer win, You lose!")
                    else:
                        user_continue_draw = False
                        print("Computer win, You lose!")
            more_card = input("Do you want to get another card? Input 'y' or 'n':\n")
            if more_card == 'y':
                player_cards.append(random.sample(cards, k=1)[0])
                current_player_score()
                play_card()
            else:
                while current_computer_score < 17:
                    for number in [0, len(cards)]:
                        computer_cards.append(random.sample(cards, k=number)[0])
                user_continue_draw= False
    play_card()
    if current_computer_score > 21:
        print(f"Your final hand: {player_cards}, final score: {current_player_score}\n"
              f"Computer's final hand: {computer_cards}, final score: {current_computer_score}")
        print("You Win!")
    else:
        if current_computer_score > current_player_score:
            print(f"Your final hand: {player_cards}, final score: {current_player_score}\n"
                  f"Computer's final hand: {computer_cards}, final score: {current_computer_score}")
            print("You lose!")
        elif current_computer_score < current_player_score:
            print(f"Your final hand: {player_cards}, final score: {current_player_score}\n"
                  f"Computer's final hand: {computer_cards}, final score: {current_computer_score}")

            print("You Win!")
        else:
            print(f"Your final hand: {player_cards}, final score: {current_player_score}\n"
                  f"Computer's final hand: {computer_cards}, final score: {current_computer_score}")
            print("It is a draw!")

#
#                         #task 5: If an ace is drawn, count it as 11.
#         # But if the total goes over 21, count the ace as 1 instead.
#         #     if 11 in computer_cards:
#         #         if current_computer_score > 21:
#         #            index = computer_cards.index(11)
#         #            computer_cards[index]=1
#         #     if
#     #task 6: Reveal computer's first card to the user.
#             print(f"Your cards: {player_cards}, current score: {sum(player_cards)}\n"
#                   f"Computer's first card: {computer_cards[0]}")
#     #task 7: Game ends immediately when user score goes over 21
#         # or if the user or computer gets a blackjack.
#             current_computer_score = sum(computer_cards)
#             current_player_score = sum(player_cards)
#             if current_player_score>21:
#                 continue_game = False
#                 print("You lose!")
#     #task 8: Ask the user if they want to get another card.
#
#     # task 9: Once the user is done and no longer wants to draw any more cards, let the computer play.
#     # The computer should keep drawing cards unless their score goes over 16.
#             while more_card == "y":
#                 player_cards.append(random.sample(cards, k=1)[0])
#                 current_player_score = sum(player_cards)
#                 print(f"Your cards: {player_cards}, current score: {sum(player_cards)}\n"
#                       f"Computer's first card: {computer_cards[0]}")
#                 if current_player_score > 21:
#                     continue_game = False
#                     print("You lose!")
#                 else:
#                     more_card = input("Do you want to get another card? Input 'y' or 'n':\n")
#             if more_card =="n":
#                 for number in cards:
#                     if sum(computer_cards)>16:
#                         break
#                     computer_cards.append(number)
#                 final_player_score = sum(player_cards)
#                 final_computer_score=sum(computer_cards)
#
#
#     #task 10: Compare user and computer scores and see if it's a win, loss, or draw.
#
#     #task 11: Print out the player's and computer's final hand and their scores at the end of the game.
#
# #task 12: After the game ends, ask the user if they'd like to play again.
#         # Clear the console for a fresh start.
#     blackjack()
#     if_play=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
#     if if_play == 'y':
#         print("\n"*100)
#         blackjack()
#     else:
#         print("Bye, have a great day!")

else:
    print("Go away!")
