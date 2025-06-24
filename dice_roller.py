import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def roll_dice():
    print("Rolling the dice", end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")
    time.sleep(0.3)
    dice_face = random.randint(1, 6)
    show_dice_face(dice_face)

def show_dice_face(number):
    faces = {
        1: ["┌───────┐",
            "│       │",
            "│   ●   │",
            "│       │",
            "└───────┘"],

        2: ["┌───────┐",
            "│ ●     │",
            "│       │",
            "│     ● │",
            "└───────┘"],

        3: ["┌───────┐",
            "│ ●     │",
            "│   ●   │",
            "│     ● │",
            "└───────┘"],

        4: ["┌───────┐",
            "│ ●   ● │",
            "│       │",
            "│ ●   ● │",
            "└───────┘"],

        5: ["┌───────┐",
            "│ ●   ● │",
            "│   ●   │",
            "│ ●   ● │",
            "└───────┘"],

        6: ["┌───────┐",
            "│ ●   ● │",
            "│ ●   ● │",
            "│ ●   ● │",
            "└───────┘"],
    }

    for line in faces[number]:
        print(line)

def main():
    while True:
        user_input = input("\nPress Enter to roll the dice or type 'q' to quit: ").lower()
        if user_input == 'q':
            print("Goodbye!")
            break
        clear_screen()
        roll_dice()

if __name__ == "__main__":
    main()
