import random

def Rolle_dic():
    while True:
        input("Press Enter to roll the dic.. :)")
        print("You rolled..!", random.randint(1, 10))
        again=input("Roll again? (Y/N)").lower()
        
        if again != 'y':
            break


Rolle_dic()
        