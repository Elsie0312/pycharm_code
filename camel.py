import random

print('You have stolen a camel to make your way across the great Mobi desert.')
print("Your enemies want their camel back and are chasing you down!")
print("Survive your desert trek and out run the enemies.")


# this will be the function we will use to run the “main” part of our game
def main():
    # initialize all the variables that will be used in this game.
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    enemies_distance = -20
    canteen_drinks = 5
    done = False
    oasis = 4

    while not done:
        print("A. Drink from your canteen")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed")
        print("D. Stop for the night")
        print("E. Status check.")
        print("Q. Quit")

        choice = input("What do you choose? Pick wisely! ")

        if choice.upper() == 'Q':
            done = True
        elif choice.upper() == 'E':
            print('Miles traveled: %s' % miles_traveled)
            print('Drinks in canteen: %s' % canteen_drinks)
            print('The enemies are %s' % (miles_traveled - enemies_distance), 'miles behind you.')
        elif choice.upper() == 'D':
            camel_tiredness = 0
            print("Your camel is a happy camper!")
            enemies_distance += random.randrange(7, 14)
        elif choice.upper() == 'C':
            miles_traveled += random.randrange(10, 20)
            print("You've traveled %s" % miles_traveled, 'miles.')
            thirst += 1
            camel_tiredness += random.randrange(1, 3)
            enemies_distance += random.randrange(7, 14)
        elif choice.upper() == 'B':
            miles_traveled += random.randrange(5, 12)
            print("You've traveled %s " % miles_traveled, 'miles.')
            thirst += 1
            camel_tiredness += 1
            enemies_distance += random.randrange(7, 14)
        elif choice.upper() == 'A':
            if canteen_drinks > 0:
                canteen_drinks -= 1
                thirst = 0
            else:
                print('Error: you are out of canteen drinks')
        else:
            print("Invalid input. Pick only the letters 'A', 'B', 'C', 'D', 'E', or 'Q'")

        if 4 < thirst <= 6:
            print('You are thirsty.')
        elif thirst > 6:
            print('You died of thirst!')
            done = True
        if 5 < camel_tiredness <= 8:
            print('Your camel is getting tired.')
        elif camel_tiredness > 8:
            print('Your camel is dead.')

        if (miles_traveled - enemies_distance) == 0:
            play_again = input('The enemies have caught up to you. Play again? Y/N')
            if play_again.upper() == 'Y':
                done = False
            elif play_again.upper() == 'N':
                print('Maybe a different day...see you around!')
            else:
                print('Invalid input')
        elif (miles_traveled - enemies_distance) <= 15:
            print('The enemies are getting close!')

        if miles_traveled >= 200 and ((miles_traveled - enemies_distance) != 0):
            print('You have won the game!')
            done = True

        if oasis == random.randrange(0, 20) and (choice == 'E' or choice == 'D'):
            print('''You have found an oasis! Rest your camel and quench your thirst,
           you lucky duck, you!''')
            canteen_drinks = 5
            thirst = 0
            camel_tiredness -= 2


if __name__ == "__main__":
    main()
