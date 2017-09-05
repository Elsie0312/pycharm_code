import random, sys

ans = True

while ans:
    question = input("Ask a question…if you dare")

    answers = random.randint(1,6)

    if question == "q":
            sys.exit()

    elif answers == 1:
            print("NO")

    elif answers == 2:
            print("Yaaaasssss")

    elif answers == 3:
            print("ummmmm maybe?")

    elif answers == 4:
            print("idk tbqh")

    elif answers == 5:
            print("definitely")

    elif answers == 6:
            print("ask me tomorrow")

