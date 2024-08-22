import cowsay, csv
from random import choice
import sys, json

def main():
    user_choice()
    riddle()
    joke()
    ask_questions()

def user_choice():
    ans = input("Do you wanna hear some jokes or maybe you're feeling clever and wanna solve some riddles? (yes iam / yepp) ").strip().lower()
    while True:
        if ans[0] == "y":
            response = input("\nPlease choose \n1.Riddles, \n2.Jokes \n3.Question asking \n4.Exit the program \n").lower()
            
            #calling the functions according to the user response
            if response == "1":
                riddle()
            elif response == "2":
                joke()
            elif response == "3":
                ask_questions()
            elif response == "4":
                sys.exit("Thank you for playing, had a fun time with you!")
            else:
                raise ValueError
            # return response   #this ends the loop after user gives a response
        
        elif ans[0] == "n":
            ans = input("You have to say yes :( ").lower()

            if ans[0] == "n":
                ans = input("Pleaasee? ").lower()

                if ans[0] == "n":
                    cowsay.cow("You made me sad")
                    sys.exit()
                    
                elif ans[0] == 'y':
                    print("\nYayyy")

            elif ans[0] == "y":
                print("\nYayyy")
        else:
            raise TypeError

def riddle():
    column= []
    ans = []
    print("\nooo okay! lets see if you can crack this riddle.")
    while True:
        with open("before.csv", "r", newline= '') as file:
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
                        print("Thats correct!!")

                        response = input("Do you wanna continue solving more riddles? (y/n) ")
                        if response == "n":
                            user_choice()
                        elif response == "y":
                            print("alright!\n")
                            response = "0"
                        else:
                            raise ValueError

                if match == False:  #checking after loop
                    response = input("Its okay, do you wanna try again? (y/n) ")
                    if response == "n":
                        user_choice()
                    elif response == "y":
                        print("\n\talright!\n")
                        response = "0"
                    else:
                        raise ValueError

def joke():
    column = []
    print("\nLets hear some jokes then\n")

    while True:
        with open("before.csv", "r", newline='') as file:
            csv_reader = csv.DictReader(file)

            for line in csv_reader: 
                column.append(line['jokes'])
            cowsay.fox(choice(column))

            ans = input("That was funny LOL\nDo you wanna hear some more jokes? (y/n) ")
            if ans == "n":
                #for now exiting the code
                user_choice()
            elif ans == "y":
                print("sure!\n")
                ans = "1"  #setting the ans to "1" so that the above loop (that works only if the answer is "1" is run)
            else:
                raise ValueError                


def ask_questions():
    cowsay.cow("Ask me any question and ill answer it\n If you wanna go to menu then press \"E\" anytime")
    while True:
        questions = input()
        if questions == "E":
            user_choice()
            
        else:
            with open("responses.json", "r") as new_file:
                reader = json.load(new_file)  #loading the json file
            cowsay.cow(choice(reader))


if __name__ == "__main__":
    main()
