import cowsay
import csv
import json
import sys
from random import choice

cowsay_char = [cowsay.beavis, cowsay.cheese, cowsay.cow, cowsay.daemon, cowsay.dragon, cowsay.fox, cowsay.ghostbusters, 
               cowsay.kitty,cowsay.meow, cowsay.miki, cowsay.milk, cowsay.octopus, cowsay.stimpy, 
               cowsay.turkey, cowsay.turtle, cowsay.tux]

def main():
    user_choice()
    riddle()
    joke()
    ask_questions()
    write_questions()

def user_choice():
    ans = input("Are you ready to play? (yes /no /e = exit): ").strip().lower()
    while True:
        if ans == "y" or ans == "yes":
            print("\n1. Riddles \n2. Jokes \n3. Questions ")
            response = input("\nChoose anyone of the above: ").lower()
                
            #calling the functions according to the user response
            if response == "1":
                riddle()
            elif response == "2":
                joke()
            elif response == "3":
                ask_questions()
            else:
                raise ValueError("\nPlease choose from the list 😟")
            # return response   #this ends the loop after user gives a response

        elif ans == "n" or ans == "no":
            ans = input("You have to say yes :( ").lower()

            if ans == "n" or ans == "no":
                cowsay.cow("You made me sad")
                sys.exit()
                        
            elif ans == "y" or ans == "yes":
                print("\nYayyy")

            else:
                print("Invalid response. Exiting...")
                sys.exit()

        elif ans == "e":
            sys.exit("\nThank you for playing, had a fun time with you! 😙")
            
        else:
            print("\nInvalid input. Please press 'y', 'n' or 'e' to exit")
            ans = input("\nAre you ready to play? (yes /no /e = exit): ").strip().lower()

def riddle():
    column= []
    ans = []
    
    print("\nooo okay! lets see if you can crack this riddle.")
    while True:
        #clearing out both the lists so that after the loop is run again, the old data is deleted and the lists are being populated correctly
        column.clear()
        ans.clear()

        with open("before.csv", "r", newline= '') as file:
            csv_reader = csv.DictReader(file)

            for line in csv_reader:
                column.append(line['riddles'])
                
            character = choice(cowsay_char)
            riddle_choice = choice(column)
            character(riddle_choice)
                        
            answer = input("Enter your answer: ").lower()

            #opening the file again to make a new instance of csv_reader since it is exhaused
            with open("before.csv", "r", newline= '') as file:
                            
                csv_reader = csv.DictReader(file)
                for line in csv_reader:
                    ans.append(line['answers'])  #appending the answers to a new list
                            
                #flag, assuming users answer is incorrect
                match = False
                for i in ans:
                    if answer == i:
                        match = True

                        response = input("\nThats correct!\n\nDo you wanna continue solving more riddles? (y/n) ")
                        if response == "n" or response == "no":
                            user_choice()
                        elif response == "y" or response == "yes" :
                            print("alright!\n")
                            continue   #response = "0"
                        else:
                            raise ValueError("Please provide a valid response 🙂")

                if not match:  #checking after loop
                    response = input("incorrect, do you wanna try again? (y/n) ")
                    if response == "n" or response == "no":
                        user_choice()
                    elif response == "y" or response == "yes":
                        print("\n\talright!\n")
                        continue  #skip the rest of the loop and show a new riddle
                    else:
                        raise ValueError("Please provide a valid response 🙂")
                    
def joke():
    column = []
    print("\nLets hear some jokes then\n")

    while True:
        column.clear()
        with open("before.csv", "r", newline='') as file:
            csv_reader = csv.DictReader(file)

            for line in csv_reader: 
                column.append(line['jokes'].replace("|","\n"))

            character = choice(cowsay_char)  #randomly selecting a character from the character list(global)
            jokes_choice = choice(column)    #randomly selecting a joke from csv file
            character(jokes_choice)          #passing the joke to the animal

            ans = input("That was funny LOL\nDo you wanna hear some more jokes? (y/n) ")
            if ans == "n" or ans == "no":
                #for now exiting the code
                user_choice()
            elif ans == "y" or ans == "yes":
                print("sure!\n")
                ans = "1"  #setting the ans to "1" so that the above loop (that works only if the answer is "1" is run)
            else:
                raise ValueError("Please provide a valid response 🙂")     


def ask_questions():
    cowsay.cow("Ask me any question and ill answer it\n 1. If you wanna go back to menu press \"E\" anytime\n2. Press \"W\" to write responses\n ")
    while True:
        try:
            questions = input("Ask a question or press \"W\" to add responses: ")
            if questions == "E":
                user_choice()
            elif questions == "W":
                write_questions()
                
            else:
                with open("responses.json", "r") as new_file:
                    reader = json.load(new_file)  #loading the json file

                    response = choice(reader)
                    character = choice(cowsay_char)
                    character(response)
                    
        except FileNotFoundError:
            sys.exit("No file found")

def write_questions():
    while True:
        try:
            #reading the file before writing to it, since the data already exists in this file
            questions = input("Enter any hilarious response: ")

            with open("responses.json", "r") as new_file:
                data = json.load(new_file)

            data.append(questions)           #appending the users entry into the json file
            with open("responses.json", "w") as new_file:     #writing the appended data to the file
                json.dump(data, new_file, indent = 4)

            response = input("\nDone!\n\nPress \"M\" if you want to add more , \"E\" to exit: ")
            if response == "E":
                user_choice()
            elif response == "M":
                continue
            else:
                print("Please enter the correct response")
                sys.exit()

        except FileNotFoundError:
            sys.exit("No file found")
                
if __name__ == "__main__":
    main()