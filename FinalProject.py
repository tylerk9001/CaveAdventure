import time
__author__ = 'Tyler Kautz'

# TODO #1: Define a function that checks if the user inputs the correct choice of left (L)(l) or (R)(r).
def choiceLR():
    choice = 'a'
    allowedChars = 'rRlL'
    while (len(choice) != 1 or choice not in allowedChars):
        choice = input('\nEnter your room choice, right (r)(R) or left (l)(L)):')
    return choice


# Define a function that checks if the user inputs the correct choice of left (L)(l), (R)(r) or forward (f)(F).
def choiceLRF():
    choice = 'a'
    allowedChars = 'rRlLFf'
    while (len(choice) != 1 or choice not in allowedChars):
        choice = input('\nEnter your room choice, right (r)(R), left (l)(L), or forward (f)(F):')
    return choice


# Allows user to grab an item that they find and checks user input
def grab():
    choice = 'a'
    allowedChars = 'Gg'
    while (len(choice) != 1 or choice not in allowedChars):
        choice = input('Press (G)(g) to grab what you found:')
    return choice

# Allows user eat when prompted to and checks user input
def eat():
    choice = 'a'
    allowedChars = 'Ee'
    while (len(choice) != 1 or choice not in allowedChars):
        choice = input('Press (E)(e) to eat:')
        if (choice == 'E' or choice == 'e'):
            print('You ate a snack!\n')
    return choice

# Allows user drink when prompted to and checks user input
def drink():
    choice = 'a'
    allowedChars = 'Dr'
    while (len(choice) != 1 or choice not in allowedChars):
        choice = input('Press (D)(d) to drink:')
        if (choice == 'D' or choice == 'd'):
            print('You drank some water!\n')
    return choice


# TODO #2: Define a function that checks if the user still has food left.
def foodChecker(health,food,water):
    if food >= 0:
        return True
    else:
        finalDescription(health, food, water)
        print('You have failed to reach the end of the cave because you ran out of food and needed to eat!')
        print('The game is now over!')
        quit()


# TODO #3: Define a function that checks if the user still has water left.
def waterChecker(health,food,water):
    if water >= 0:
        return True
    else:
        finalDescription(health, food, water)
        print('You have failed to reach the end of the cave because you died. You ran out of water and needed to drink '
              'to stay hydrated!')
        print('The game is now over!')
        quit()


# TODO #3: Define a function that checks if the user is still alive.
def healthChecker(health,food,water):
    if health <= 0:
        print('You have failed to reach the end of the cave because you died. Your health is 0 resulting in death!')
        print('Your game is now over!')
        finalDescription(health, food, water)
        quit()
    else:
        return True


# TODO #4: Print the final statements (winner or loser) based on how the user finishes.
def gameWinner(correct_path,health,food,water):
    if correct_path >= 6:
        print('Congratulations, you have successfully made it out of the cave!')
        finalDescription(health, food, water)
        quit()

def gameLoser(correct_path,health,food,water):
    if correct_path < 6:
        print('You didn\'t take the right path in the cave. You have not made it out of the cave.')
        finalDescription(health,food,water)


# TODO #5: Define a function that tells the user what they finished with.
def finalDescription(health,food,water):
    print('You finished with the following: \n')
    print('Your health at', health,'.')
    print('A total of', food, 'unit(s) of food.')
    print('A total of', water, 'bottle(s) of water.')


# TODO #6: Define a function that will tell the user how much supplies they have left each time.
def scenarioDescription(health,food,water):
    print('Your health is', health)
    print('You have', food, 'unit(s) of food remaining.')
    print('You have', water, 'bottle(s) of water remaining. \n')


def main():

# TODO 7: Print the introduction description at the beginning of the game.
    print('Welcome to your adventure through this dark mysterious cave!')
    print('Your mission is to successfully travel through this cave and reach the exit without dying.')
    print('As you are on your adventure, you will have to overcome and tackle the complex struggles that will face you.')
    print('As you travel through the cave, you will eat and drink based off of your decision to avoid starvation and/or dehydration.')
    print('Eating food can also add a boost to your health to help you heal up!')
    print('You only have a certain amount of supplies to take with you, so, choose very wisely what you do with it and when you use it!')
    print('Before beginning, I must inform you about the supplies you hold. \n')

    # Starting values of variables
    correct_path = 0
    health = 100
    water = 5
    food = 5

    print('To take with you, you have:\n')
    print('1.',food,'Units of food')
    print('2.',water,'Bottles of water')
    print('3. A flashlight')
    print('4. A pocket knife')
    print('5. A first aid kit')
    print('6. A jacket')
    print('7. Yourself')
    print('Your current health stands at:',health,'\n')

# TODO 8: Wait 20 seconds before showing next line of code, forcing the reader to read the description above.
    time.sleep(20)
    print('Did you read the instructions above? Make sure you do!\n')
    time.sleep(3)


# TODO 7 (Continued)
    print('You will have a choice between traveling to the right (r)(R) or left (l)(L) room.')
    print('Based off your decision, the obstacles may become simplier or complex and require more or less food and water.\n')


# TODO 8 (Continued): Wait for user input to continue.
    input('When you are ready, press enter to begin your adventure.')
    print('')

    # Finds a flashlight
    print('Begin you go any further, look around and see if you can find any supplies that could be useful for your adventure.')
    # Waits 5 seconds before next line prints, forcing the user to read.
    time.sleep(5)
    print('You found a flashlight with batteries, and it works! Grab it and put it in your backpack!\n')
    grab()
    print('Awesome! Now get on with the adventure!')


# TODO 9: Begin the adventure through 10 different scenarios in the cave.
    # Scenario #1
    user_choice = choiceLR()

    if (user_choice == 'l' or user_choice == 'L'):
        print('You chose the left room and encountered a dark, spooky, and mysterious room and can\'t see anything, '
              'you must use your flashlight to get through the room. \n')
        correct_path = correct_path + 1
    elif (user_choice == 'r' or user_choice == 'R'):
        print('You chose the right room and encountered a cluster of poisonous spiders that crawled and '
              'bit your feet, causing you to take a seat, drink some water and recover for a few minutes. \n')
        drink()
        health = health - 15
        water = water - 1
        waterChecker(health,food,water)
        healthChecker(health, food, water)
    scenarioDescription(health, food, water)

    # Finds a helmet
    print('Check around and see if you find anything in here.')
    # Waits 5 seconds before next line prints, forcing the user to read.
    time.sleep(5)
    print('You found a helmet, put it on and make sure it is tight!\n')
    grab()
    print('Awesome! You got the helmet, now keep moving! \n')


# TODO 8: Get user input to continue
    input('When you are ready, press enter to continue your adventure.')

    # Scenario #2
    user_choice = choiceLRF()

    if (user_choice == 'l' or user_choice == 'L'):
        print('You chose the right room and found a sea cave, causing you to swim across to the other side to be able'
              'to get to the next room. During your swim you became very tired and need to eat some food. \n')
        eat()
        food = food - 1
        if health <= 90:
            health = health + 10
            healthChecker(health, food, water)
        correct_path = correct_path + 1
        foodChecker(health, food, water)
    elif (user_choice == 'r' or user_choice == 'R'):
        print('You chose the left room and tripped over a rock causing you to bump your head on a sharp cavern causing '
              'you to stop and bandage it up. \n')
        health = health - 10
        healthChecker(health, food, water)
    elif (user_choice == 'f' or user_choice == 'F'):
        print('You chose to go in to the room in front of you and found a giant salamander! Run away from it before it '
              'catches you!')
        input('Press enter to run away from the salamander!\n')
        print('Luckily you got away, sit down and drink some water before you continue.\n')
        drink()
        water = water - 1
        waterChecker(health, food, water)
    scenarioDescription(health, food, water)


# TODO 8 (Continued)
    input('When you are ready, press enter to continue your adventure.\n')

    # Scenario #3
    user_choice = choiceLR()

    if (user_choice == 'l' or user_choice == 'L'):
        print('You chose the left room and invaded a colony of bats habitat. They were extremely angry with you and '
              'bit you causing you to lose a lot of blood. \n')
        health = health - 30
    elif (user_choice == 'r' or user_choice == 'R'):
        print('You chose the right room and encountered a mud pit. You must walk through the mud to get out of this '
              'room. But, be careful that you don\'t get hit by the falling rocks above the pit! Make sure your helmet '
              'is secured tight on your head.')
        print('Take a second to eat a snack!\n')
        eat()
        food = food - 1
        foodChecker(health,food,water)
        correct_path = correct_path + 1
    scenarioDescription(health, food, water)


    # Finds a helmet
    print('As you exited the room you saw a pair of old gloves. Pick them up because they might be useful at some point.')
    time.sleep(2)
    grab()
    print('You grabbed the gloves. Now continue on...\n')


# TODO 8 (Continued)
    input('When you are ready, press enter to continue your adventure.')

    # Scenario #4
    user_choice = choiceLR()

    if (user_choice == 'l' or user_choice == 'L'):
        print('You chose the left room and encountered a wall that you can only crawl under to get through. The tunnel is '
              'just big enough for you to fit under. Make sure to drink some water before you start because you may sweat '
              'and get hot! \n')
        drink()
        water = water - 1
        waterChecker(health, food, water)
        correct_path = correct_path + 1
    elif (user_choice == 'r' or user_choice == 'R'):
        print('You chose the right room and ran into a poisonous scorpion that stung you with its tail. It injected poison into'
              'you but if you get out of the cave fast enough and see a doctor you could potentially survive. Hurry up and get out'
              'of the cave.')
        print('Drink some water and eat a snack before you go!')
        print('Now, hurry up and get out!!!\n')
        water = water - 1
        food = food - 1
        drink()
        eat()
        health = health - 50
        foodChecker(health, food, water)
        waterChecker(health, food, water)
        healthChecker(health, food, water)
    scenarioDescription(health, food, water)


# TODO 8 (Continued)
    input('When you are ready, press enter to continue your adventure.')

    # Scenario #5
    user_choice = choiceLR()

    if (user_choice == 'l' or user_choice == 'L'):
        print('You chose the left room and found a huge hole that drops 50 feet to the bottom of the cave. There is just '
              'enough room for you to squirm around the edge. Be careful, put those gloves on that you found, you can make it!!\n')
    elif (user_choice == 'r' or user_choice == 'R'):
        print('You chose the right room and found a rock wall that is about 30 feet tall. In order to get to the next '
              'room you need to climb up the wall, but it is going to take alot of energy. You need to eat and drink '
              'before you begin your climb! \n')
        drink()
        eat()
        correct_path = correct_path + 1
        water = water - 1
        food = food - 1
        if health <= 90:
            health = health + 10
        healthChecker(health, food, water)
        foodChecker(health,food,water)
        waterChecker(health, food, water)
    scenarioDescription(health, food, water)

# TODO 8 (Continued)
    input('When you are ready, press enter to continue your adventure.')

    # Scenario #6
    user_choice = choiceLR()

    if (user_choice == 'l' or user_choice == 'L'):
        print('You chose the left room and it has a burning hot pit of lava in it. You have to walk around the perimeter'
              ' of the pit without stepping in the lava. Be careful!')
        input('When you are ready to walk around the pit, press enter!')
        print('You successfully walked the perimeter without stepping in the lava! Now drink some water and take a seat '
              'before you continue through the cave. \n')
        drink()
        correct_path = correct_path + 1
        water = water - 1
        waterChecker(health,food,water)
        gameWinner(correct_path, health, food, water)
    elif (user_choice == 'r' or user_choice == 'R'):
        print('You chose the right room and face absolutely no obstacles. Lucky you!! Keep on going, you are almost there! \n')
    scenarioDescription(health, food, water)


# TODO 8 (Continued)
    input('When you are ready, press enter to continue your adventure.')

    # Scenario #7
    user_choice = choiceLRF()

    if (user_choice == 'l' or user_choice == 'L'):
        print('You ran into a snake that bit you and infected you with a disease, that has gone to your bloodstream'
              'and instantly killed you!\n')
        health = health - 100
        healthChecker(health, food, water)
    elif (user_choice == 'r' or user_choice == 'R'):
        print('You chose the right room and up ahead you see a lot of water dripping from the ceiling. Use the jacket you '
              'have so you don\'t get too wet!\n')
        correct_path = correct_path + 1
        gameWinner(correct_path, health, food, water)
    elif (user_choice == 'f' or user_choice == 'F'):
        print('You chose the room in front of you and encountered a dark, spooky, and mysterious room and can\'t see anything, '
              'you must use your flashlight to get through the room.')
        print('You are getting thirsty, drink some water before you continue.\n')
        drink()
        water = water - 1
        waterChecker(health,food,water)
    scenarioDescription(health, food, water)



# TODO 8 (Continued)
    input('When you are ready, press enter to continue your adventure.')

    # Scenario #8
    print('You had to go into the room in front of you, but, you face absolutely no obstacles. Lucky you!! Keep on going,'
          ' you are almost there!\n')
    correct_path = correct_path + 1
    gameWinner(correct_path, health, food, water)

# TODO 8 (Continued))
    input('When you are ready, press enter to continue your adventure.')

    # Scenario #9
    user_choice = choiceLRF()

    if (user_choice == 'l' or user_choice == 'L'):
        print('You chose the left room and tripped over a rock but are okay!\n')
        print('Get up and continue on!')
        correct_path = correct_path + 1
        healthChecker(health, food, water)
        gameWinner(correct_path, health, food, water)
    elif (user_choice == 'r' or user_choice == 'R'):
        print('You chose the right room and it had a small walk way that you have to go through, nothing but'
              'your body will fit, causing you to leave everything behind. You now have no food or water.\n')
        water = 0
        food = 0
    elif (user_choice == 'f' or user_choice == 'F'):
        print('You chose the room in front of you and ran into stalagmites on the ground that caused you to go a different way so '
          'that you don\'t hurt your feet.\n')
        print('You became really tired on your way back out, drink some water before you continue.\n')
        drink()
        water = water - 1
        waterChecker(health, food, water)
    scenarioDescription(health, food, water)


# TODO 8 (Continued)
    input('When you are ready, press enter to continue your adventure.')

    # Scenario #10
    user_choice = choiceLR()

    if (user_choice == 'l' or user_choice == 'L'):
        print('You chose the left room and found the exit to the cave!\n')
        correct_path = correct_path + 1
        gameWinner(correct_path, health, food, water)
    elif (user_choice == 'r' or user_choice == 'R'):
        print('You chose the right room which has a massive hole in it. You tripped and fell to your death!\n')
        print('Be a little bit more careful next time!')
        health = health - 100
        healthChecker(health,food,water)
    gameLoser(correct_path,health,food,water)

# TODO 8 (Continued)
    input('Press any key to exit and try again!')

main()