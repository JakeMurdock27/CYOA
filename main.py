import random


weapon = ["Sword", "Crossbow", "Long Sword", "Magic Sword"]
weapon_attack = 0
user_health = 100
user_xp = 10
leopard_health = 100


def stats():
    return (
        "\n" + "Health: " + str(user_health) + " / "
        "XP: " + str(user_xp) + " / "
        "Current Weapon: " + weapon[0] + "\n"
    )


def fight_stats():
    global __name__
    return (
        "\n"
        + "User Health: "
        + str(user_health)
        + " / "
        + "Leopard Health: "
        + str(leopard_health)
        + " / "
        + " XP: "
        + str(user_xp)
        + " / "
        "Current Weapon: " + weapon[0] + "\n"
    )


def start_game():
    name = input("Please type your name: \n")
    print("\nWelcome", name + ", to this wonderful adventure!\n")
    print("Here are your current stats: ")
    print(stats())
    crossroads()


def crossroads():
    answer = input(
        "Let us begin by setting the scene...\nYou are on a dirt road. The sun is high in the sky. It looks to be about mid day. You wander up to a cross road and you see that you can either go straight, left or right. Which way would you like to go? (Left/Right/Straight)\n"
    ).lower()
    if answer == "right":
        right()
    if answer == "left":
        left()
    if answer == "straight":
        straight()
    else:
        print("That is not a valid option. Lets try again.")
        return crossroads()


def right():
    global user_xp
    answer = input(
        "\nWonderful choice! You start walking to the right and as you continue on your path you see a forest on the horizon. As you continue on your path toward the forest, you start to realize that you are getting an uneasy feeling but you can't quite place it. As you look down at the road it does still look to be well traveled. What would you like to do? \n(continue/turn around) "
    ).lower()
    if answer == "continue":
        answer = input(
            "\nYou decide to continue on even with the uneasy feeling. As you enter the forrest, you see that the trees are thick and the canopy makes it dark and eery. As you continue on, it starts to get colder and colder... You think you hear something rustling behind you but when you turn around to check it out there is nothing there. You keep walking and hear a sound in front of you but you can't place it. What do you do? \n(continue/turn around) "
        ).lower()
        if answer == "continue":
            return leopard()
        if answer == "turn around":
            print(
                "\nYou decide to turn around and leave. As you are walking, you start to hear the rustling get louder behind you. You turn around but can't see anything. You keep walking but you hear the rustling get louder and and louder. You start to run. The rustling continues. You start to run faster and faster! You start to come up to the edge of the forest and can see the light. As you just about to cross the threshold you trip over a root and tumble forward out of the forest. When you look up and back at the forest you can see two red eyes looking back at you!..... Looks like you got away by the skin of your teeth. Way to go!"
            )
            print("Wow look at that. Your XP increased!")
            user_xp += 10
            print(stats())
            print("Lets get you back to the start.\n")
            crossroads()
    elif answer == "turn around":
        crossroads()
    else:
        print("That is not a valid choice please try again.\n")
        right()


def left():
    answer = input("this is left").lower()
    if answer == "":
        return


def straight():
    answer = input("this is straight").lower()
    if answer == "":
        return


def attack_hit():
    global leopard_health
    global user_health
    global user_xp
    random_number = random.randint(0, 20)
    print(fight_stats())
    if user_health <= 0:
        print("You lost all of your health. It was a brave fight.")
        quit()
    if leopard_health <= 0:
        print("You have defeated the leopard and won the game!! Way to go!")
        user_xp += 5000
        user_health = 100
        quit()
    elif random_number >= 13:
        leopard_health -= 25
        print("You hit it!\n")
        answer = input("Would you like to attack again? \n(attack/run) ").lower()
        if answer == "attack":
            attack_hit()
        if answer == "run":
            print(
                "\nYou decide to turn around run! As you are running, you start to hear the leopard get louder behind you! It is chasing you! You start to run faster and faster! You  come up to the edge of the forest and can see the light. As you just about to cross the threshold you trip over a root and tumble forward out of the forest. When you look up and back at the forest you can see two red eyes looking back at you!..... Looks like you got away by the skin of your teeth. Way to go!"
            )
            print("Wow look at that. Your XP increased!")
            user_xp += 10
            print(stats())
            print("Lets get you back to the start.\n")
            crossroads()
    elif random_number < 13:
        user_health -= 25
        answer = input(
            "You missed! The leopard take a strike and hits! You can't take much more of that! Would you like to attack again? \n(attack/run) "
        ).lower()
        print(fight_stats())
        if answer == "attack":
            attack_hit()
        if answer == "run":
            print(
                "\nYou decide to turn around run! As you are running, you start to hear the leopard get louder behind you! It is chasing you! You start to run faster and faster! You  come up to the edge of the forest and can see the light. As you just about to cross the threshold you trip over a root and tumble forward out of the forest. When you look up and back at the forest you can see two red eyes looking back at you!..... Looks like you got away by the skin of your teeth. Way to go!"
            )
            print("Wow look at that. Your XP increased!")
            user_xp += 10
            print(stats())
            print("Lets get you back to the start.\n")
            crossroads()
    else:
        quit()


def leopard():
    answer = input(
        "You walk forward slowly and surely with you hand on the hilt of your sword. As you take your next step the bushes in front of you start to rustle. When all of the sudden, out of the bushes jumps a black leopard!! It is growling and bearing its teeth. It appears that it hasn't eaten in weeks!! Now in the moment you do realize that you have two options. Grab the food from you bag or draw the sword that is currently in your hand. What would you like to do? \n(fight/feed) "
    ).lower()
    if answer == "fight":
        print(
            "You pull out your sword and the leopard lunges. You narrowly escape by jumping out of the way!"
        )
        answer = input("What do you do next?! \n(fight/run) ").lower()
        if answer == "fight":
            stats()
            print("With your sword in hard you take a swipe at the leopard!\n")
            attack_hit()
        if answer == "run":
            print(
                "You take off in the other direction. Now you are fast but you aren't faster than a leopard!! You make it to the clearing of the forrest"
            )


def main():
    start_game()


if __name__ == "__main__":
    main()
