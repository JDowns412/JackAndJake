#Import Statements
import random


# Methods
def draw_card() -> int:
    card_value=random.randint(2,11)
    if card_value==11
        user_choice=input("Do you want your ace to be a 1 or 11?")
        # if user_choice==11:
    return card_value


# Here's where all the code for our blackjack game goes
def run_game() -> None:
    # Variables:
    hand=[]

    #Draw our starting hand
    for i in range(2):
        hand.append(draw_card())

    #Asking if you want your ace to be 1 or 11
    




    print(hand) 





def main() -> None:
    try:
        run_game()
    except (KeyboardInterrupt, EOFError):
        print("\nThere was a problem. Exiting game. Goodbye.")
        sys.exit(0)

# Start
if __name__ == "__main__":
    main()










