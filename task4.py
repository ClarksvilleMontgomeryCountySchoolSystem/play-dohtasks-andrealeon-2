
"""
ANSWER BOX - Copy the strings you need:

"standing up or flopped down?"
") Keep it round.\n"
") Attach two pieces using {color2} hanging downward.\n"
") Name this creation: "Dog""
") Roll a smaller ball using {color1} for the head.\n"
"hot dog or round like a ball?"
") Roll a ball using {color1} for the body.\n"
") Attach two pointed pieces using {color2} upright.\n"
") Attach the head to the body.\n"
") Add four legs using {color1}, a small tail using {color2}, two eyes, and a nose.\n"
") Stretch it out.\n"
"""

def main():
    color1 = "Blue"
    color2 = "Red"
    print(f"1) Roll a ball using {color1} for the body.\n")
    choice1 = input("hot dog or round like a ball? ")
    if choice1 == "hot dog":
        print("2) Stretch it out.\n")
    else:
        print("2) Keep it round.\n")
    print(f"3) Roll a smaller ball using {color1} for the head.\n")
    print("4) Attach the head to the body.\n")
    choice2 = input("standing up or flopped down? ")
    if choice2 == "standing up":
        print(f"5) Attach two pointed pieces using {color2} upright.\n")
    else:
        print(f"5) Attach two pieces using {color2} hanging downward.\n")
    print(f"6) Add four legs using {color1}, a small tail using {color2}, two eyes, and a nose.\n")
    print('7) Name this creation: "Dog"')



if __name__ == "__main__":
    main()
