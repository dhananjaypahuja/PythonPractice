import random

def main():
    answer = random.randint(1,100)
    high_range = 100
    low_range = 1

    print("Cheat: ", answer)

    while True:
        try:
            guess = int(input("Guess the number between 1 and 100: "))
            if guess in range(1, 101):
                if answer == guess:
                    print("Congratulations! Correct guess!")
                    break
                elif answer > guess:
                    print("Too Low!")
                    low_range = guess
                    print(f"New Guess Range: {low_range} to {high_range}")
                elif answer < guess:
                    print("Too High!")
                    high_range = guess
                    print(f"New Guess Range: {low_range} to {high_range}")
            else:
                print("Invalid range!")
        except ValueError:
            print("Please enter a valid integer value.")


if __name__ == '__main__':
    main()