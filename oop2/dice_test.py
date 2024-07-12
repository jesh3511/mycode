#!/usr/bin/python3
"""RZFeeser | Alta3 Research
Creating a simple dice program utilizing classes."""


# imports from cheadice.py (this is in the local directory)
from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice

def main():
    """run-time code"""

    # create two cheater objects
    x = int(input("enter the amount of players"))
    player = [Player() for i in range(x)]
    for num in player:
        player.append(num)
    player[0].roll()
    player[0].cheat()
    cheater1 = Cheat_Swapper() # ability is to change 3rd dice roll to 6
    cheater2 = Cheat_Loaded_Dice() # increase all rolls by +1 provided they are < 6

    # both players take turns
    #cheater1.roll()
    #cheater2.roll()

    # both players use their cheat methods
    #cheater1.cheat()
    #csheater2.cheat()

    print(f"Player 1 rolled {player[0].get_dice()}")
    print(f"Cheater 2 rolled {cheater2.get_dice()}")

    if sum(player[0].get_dice()) == sum(player[0].get_dice()):
        print("Draw!")

    elif sum(player[0].get_dice()) > sum(player[0].get_dice()):
        print("Cheater 1 wins!")

    else:
        print("Cheater 2 wins!")

if __name__ == "__main__":
    main()
