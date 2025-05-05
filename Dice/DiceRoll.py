import random

def roll_dice(dice: int = 2):
    rolls = []
    for _ in range(dice):
        rolls.append(random.randint(1,6))
    return rolls


def __main__():
    counter = 0
    valid = {"yes", "no", "y" , "n"}
    
    while True:
        try:
            dice = int(input("How many dice to roll?: "))
            break
        except ValueError:
            print("Integer value only!")
        finally:
            print("Starting Game!")

    # name = input("Enter your name (default is 'Guest'): ") or "Guest"



    while True:
        option = input("Do you want to roll? (y/n): ").lower()
        if option in valid:
            if option[0] == "y":
                print(roll_dice(dice))
                counter += 1
                print("Chance: ", counter)
            elif option[0] == "n":
                print("Terminating!")
                return
        else:
            print("Say Yes or No!")

if __name__ == "__main__":
    __main__()