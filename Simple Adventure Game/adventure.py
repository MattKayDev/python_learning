from re import A


name = input("Type your name: ")
print("Welcome", name, "to this adventure!")
while True:
    print(name, "your adventure beings now!")
    answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ")
    if answer.lower() == "left":
        q2 = input("Okay, you come to a river and can walk around it or swim across it? Type walk to walk and swim to swim: ")
        if q2.lower() == "swim":
            print("You swam across the river and were eaten by shark!")
        elif q2.lower() == "walk":
            print("You walked for many miles, ran out of water and you lost the game!")
        else:
            print("Not a valid option. You lose.")
    elif answer.lower() == "right":
        q3 = input("You came to a bridge, it looks woobly, do you want to cross it or go back? Type cross to corss the bridge or back to go back: ")
        if q3.lower() == "cross":
            print("You crossed the bridge")
            q4 = input("You kept walking and meet a stranger sitting under the tree. Do you want to talk to him? Type yes to talk or no to carry on walking: ")
            if q4.lower() == "yes":
                print("You asked the stranger does he need any help?")
                print("He quickly jumped up, stabbed you with a knife and robbed off with your gold. You lose.")
            elif q4.lower() == "no":
                print("You carried on walking but looking back you noticed that the stranger has disappeared.")
                q5 = input("Do you go back to check what happened? Type yes to go back or type no to carry on walking: ")
                if q5.lower() == "yes":
                    print("He jumped out of the bushes with a knife and cut you.")
                    print("You started bleeding very heavily. He took off with your gold.")
                    print("You lose.")
                elif q5.lower() == "no":
                    print("You continued on your journey and completed the game! You WIN!")
                    break
                else: print("Not a valid option. You lose.")
            else:
                print("Not a valid option. You lose.")
        elif q3.lower() == "back":
            print("You tried going back but you tripped and fell down the mountain. You lost the game.")
        else:
            print("Not a valid option. You lose.")
    else: 
        print("Not a valid option. You lose.")

print("You won the game. Congratulations!")