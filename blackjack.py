#Import Statements
import random
import sys

# Makes a random value for your new card (after you hit)
def draw_card(current_hand) -> int:
    card_value=random.randint(2,11)
    
    # Checking if you have an ace
    if card_value==11:
        user_choice=input(f" You drew a ace! Your hand is: {current_hand} \nDo you want your ace to be a 1 or 11?")
        card_value=int(user_choice)
    return card_value

# Asking the user if they want to hit or stand
def check_for_hit() -> None:
    # Hit or stand mechanism
    proper_answer=False
    while (proper_answer==False):
        user_input=input("Do you want to hit or stand?")
        if user_input=="stand":
            proper_answer=True
        elif user_input=="hit":
            proper_answer=True
        else:
            proper_answer=False
            print("that was not a viable answer, try again")
    return user_input

# Tells you your hand
def print_hand(current_hand, busted=False, dealers_score=None) -> None:
    if busted:
        print(f"Your hand was: {current_hand}, which scored to: {sum(current_hand)}, and the dealers hand was {dealers_score}")
    else:
        print(f"Your hand is: {current_hand}, which scores to: {sum(current_hand)}")

# Here's where all the code for our blackjack game goes
def run_game() -> None:
    # Variables:
    hand=[]

    # Draw our starting hand
    for i in range(2):
        hand.append(draw_card(hand))
    
    # Gives the dealer a score and then checks against yours
        dealers_score=random.randint(2,21)

    # Main game loop
    user_choice ="hit"
    while (user_choice=="hit"):
        print_hand(hand)

        # Ask the user if they want to hit or stand
        user_choice=check_for_hit()
        if user_choice=="hit":
            #Adds a card to the users hand
            hand.append(draw_card(hand))

        
        # Checks if you have busted or not
        if sum(hand)>21:
            # Automatically save you when you are going to bust
            if 11 in hand:
                index_of_ace = hand.index(11)
                hand[index_of_ace]=1
                print("We downgraded your ace to save you from busting.")
            else:
                print("You bust!")
                print_hand(hand, True, dealers_score)
                sys.exit(0)

    
   
    print(f"The dealers score was: {dealers_score}")
    if dealers_score>sum(hand):
        print("You lost!")
    elif dealers_score<sum(hand):
        print("You win!")
    else:
        print("You tied!")


def main() -> None:
    try:
        run_game()
    except (KeyboardInterrupt, EOFError):
        print("\nThere was a problem. Exiting game. Goodbye.")
        sys.exit(0)

# Start
if __name__ == "__main__":
    main()










