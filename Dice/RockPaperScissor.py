import random
from pprint import pprint as pp

rps_choices = ["rock", "paper", "scissor"]
valid_choices = ["yes", "no", "y", "n"]

class Node:
    def __init__(self, value: str = None):
        self._value = value
        self.next = None
    
    def get_value(self):
        return self._value

class RockPaperScissor:

    rock = Node("rock")
    paper = Node("paper")
    scissor = Node("scissor")

    rock.next = paper
    paper.next = scissor
    scissor.next = rock

    # Test circular list
    def print_circular():
        head = RockPaperScissor.rock
        seen = head
        while True:
            pp(head.get_value())
            head = head.next
            if head == seen:
                break


    def main():

        win = 0
        lose = 0
        draw = 0
        pp("Lets Play Rock Paper Scissior!")

        while True:
            comp_choice = random.choice(rps_choices)
            print("Cheat: ", comp_choice)
            print(f"Score (w/l/d): {win} / {lose} / {draw}")
            print("Total Rounds: {}".format(sum((win, lose, draw))))        # convert to tuple for passing to sum
            
            while True:
                try:
                    player_choice = str(input(f"Select one of the following choices:  \n {rps_choices} \n"))
                    if player_choice.strip().lower() not in rps_choices:
                        raise ValueError("Invalid Choice!")
                    else:
                        player_node = Node(player_choice)
                        head = RockPaperScissor.rock
                        while player_node.get_value() != head.get_value():
                            head = head.next
                        if head.get_value() == comp_choice:
                            print("Draw!")
                            draw += 1
                            break
                        elif head.next.get_value() == comp_choice:
                            print("You Lose!")
                            lose += 1
                            break
                        else:
                            print("You Win!")
                            win += 1
                            break
                except ValueError as e:
                    pp(e)
                    continue
            
            try:
                play = input("Continue? (y/n) ")
                if not isinstance(play, str) or play.strip().lower() not in valid_choices:
                    raise ValueError("Invalid Choice!")
                else:
                    if play[0] == "y":
                        continue
                    else:
                        break
            except ValueError as e:
                print(e)
                continue



if __name__ == '__main__':
    RockPaperScissor.main()