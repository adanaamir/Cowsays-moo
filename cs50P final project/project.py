import cowsay, csv
from random import choice
import sys

def main():
    user_choice()
    riddle()
    joke()

def user_choice():
    ans = input("Do you wanna hear some jokes or maybe you're feeling clever and wanna solve some riddles? (yes iam / yepp) ").strip().lower()
    while True:
        if ans[0] == "y":
            advice = input("Cool! Riddles or jokes? (0 = riddles / 1= joke) ").lower()
            
            #calling the functions according to the user response
            if advice == "0":
                riddle()
            elif advice == "1":
                joke()
            else:
                raise ValueError
            # return advice   #this ends the loop after user gives a response
        
        elif ans[0] == "n":
            ans = input("You have to say yes :( ").lower()

            if ans[0] == "n":
                ans = input("Pleaasee? ").lower()

                if ans[0] == "n":
                    cowsay.cow("You made me sad")
                    sys.exit()
                    
                elif ans[0] == 'y':
                    print("Yayyy")

            elif ans[0] == "y":
                print("Yayyy")
        else:
            raise TypeError

def riddle():
    column= []
    ans = []
    with open("before.csv", "r", newline= '') as file:
        print("\nooo okay! lets see if you can crack this riddle.\n")
        csv_reader = csv.DictReader(file)

        for line in csv_reader:
            column.append(line['riddles'])
        cowsay.fox(choice(column))
            
        answer = input("Enter your answer: ").lower()

        #opening the file again to make a new instance of csv_reader since it is exhaused
        with open("before.csv", "r", newline= '') as file:
                
            csv_reader = csv.DictReader(file)
            for line in csv_reader:
                ans.append(line['answers'])  #appending the answers to a new list
                
            #flag
            match = False
            for i in ans:
                if answer == i:
                    match = True
                    print("Alright thats correct")

            if match == False:  #checking after loop
                print("Its okay, try again...")

def joke():
    column = []
    print("\nLets hear some jokes then\n")
    with open("before.csv", "r", newline='') as file:
        csv_reader = csv.DictReader(file)

        for line in csv_reader: 
            column.append(line['jokes'])
        cowsay.fox(choice(column))

def write_data():
    ...


if __name__ == "__main__":
    main()
