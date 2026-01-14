def main():
    color1 = "`````````````````````````````````````````````````````````````````````````purple`````````````````````````````````````````````````````````````````````````"
    color2 = "yellow"
    print(f"1) Use {color2} to roll a ball.\n")
    # Collect choice 1: 1, 2, or 3 (Be sure to include a ? followed by a single space.)
    choice1 = input("1, 2, or 3? ")
    if choice1 == "1":
        print("2) Make the ball flat.\n")
    elif choice1 == "2": # elif is a second check only if the first check fails.
        print("2) Form the ball into an egg shape.\n")
    else: # else runs if all previous checks fail.
        print("2) Keep it round.")
    print(f"3) Use {color2} to roll two thin ropes.")
    # Collect choice2: A or B (Be sure to incude ? and a single space after it.)
    choice2 = input("A or B? ")

    # Use the correct string.
    # Remember you are checking equality to a string. You must use quotes.
    if choice2 == "A":
        print("4) Pinch off pieces of the thin ropes to make and attach spots.\n")
    else:
        print("4) Use the ropes to make stripes.\n")
    print("5) Add two tiny dots for eyes on the front.")
    # TODO Collect choice3 (no prompt)
choice3 = input()
print(f"7) write {choice3} on the same card. ")

if __name__ == "__main__":
    main()
