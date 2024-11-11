import random

def main():
    x = user()
    y = comp()
    print(f"User: {x}")
    print(f"Computer: {y}")
    if x == y:
        print("It's a tie!")
    elif x == "rock" and y == "scissor":
        print("User wins!")
    elif x == "scissor" and y == "paper":
        print("User wins!")
    elif x == "paper" and y == "rock":
        print("User wins!")
    else:
        print("Computer wins!")

def user():
    x = get_input()
    user = ""
    if x == 1:
        user = "rock"
    elif x == 2:
        user = "paper"
    else:
        user = "scissor"
    return user


def comp():
    comp = random.choice(["rock", "paper","scissor"])
    return comp

def get_input():
    while True:
        try:
            n = int(input("rock(1), paper(2) or scissor(3) ? "))
            if n not in range(1, 4):
                raise ValueError
        except ValueError:
            pass
        else:
            return n

main()