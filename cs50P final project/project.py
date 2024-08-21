import cowsay, csv
from random import choice
import sys

def main():
    user_answer = user_choice()
    read_data(user_answer)

def user_choice():
    ans = input("Do you wanna hear some jokes or maybe you're feeling clever and wanna solve some riddles? (yes iam / yepp) ").strip().lower()
    while True:
        if ans[0] == "y":
            advice = input("Cool! Riddles or jokes? (0 = riddles / 1= joke) ").lower()
            return advice   #this ends the loop after user gives a response
        
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

def read_data(user_ans):
    column= []
    ans = []
    with open("before.csv", "r", newline= '') as file:
        if user_ans == "0":
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
                
                for i in ans:
                    if answer == i:
                        print("Alright thats correct")
                    else:
                        pass
                if answer != i:  #after the loop if there the answer is wrong then print wrong instead of printing wrong for every wrong answer
                    print("hmm maybe try again...")


# def joke():
        elif user_ans == "1":

            print("\nLets hear some jokes then\n")
            csv_reader = csv.DictReader(file)

            for line in csv_reader:
                column.append(line['jokes'])
            cowsay.fox(choice(column))

        else:
            raise ValueError

def write_data():
    ...


if __name__ == "__main__":
    main()
