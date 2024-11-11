import random

def main():
    """
    Main function to run the rock-paper-scissors game.
    """
    stats = {
        "comp_wins": 0,
        "user_wins": 0,
        "ties": 0
    }

    while True:
        user_choice = user()
        comp_choice = comp()
        print(f"User: {user_choice}")
        print(f"Computer: {comp_choice}")

        if user_choice == comp_choice:
            print("It's a tie!")
            stats["ties"] += 1
        elif (user_choice == "rock" and comp_choice == "scissor") or \
             (user_choice == "scissor" and comp_choice == "paper") or \
             (user_choice == "paper" and comp_choice == "rock"):
            print("User wins!")
            stats["user_wins"] += 1
        else:
            print("Computer wins!")
            stats["comp_wins"] += 1

        for key, value in stats.items():
            print(f"{key} : {value}")

        play_again = input("Press Enter to play again or type 'quit' to stop: ").strip().lower()
        if play_again == 'quit':
            break

def user():
    """
    Get the user's choice.
    """
    choice_map = {1: "rock", 2: "paper", 3: "scissor"}
    user_input = get_input()
    return choice_map[user_input]

def comp():
    """
    Get the computer's random choice.
    """
    return random.choice(["rock", "paper", "scissor"])

def get_input():
    """
    Get and validate user input.
    """
    while True:
        try:
            n = int(input("rock(1), paper(2) or scissor(3) ? "))
            if n not in range(1, 4):
                raise ValueError
        except ValueError:
            print("Invalid input, please enter 1, 2, or 3.")
        else:
            return n

if __name__ == "__main__":
    main()
