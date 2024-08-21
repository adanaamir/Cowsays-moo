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
        else:
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


def read_data(user_ans):
    column= []
    with open("before.csv", "r", newline= '') as file:
        if user_ans == "0":
            print("ooo okay! lets see if you can crack this riddle.")
            csv_reader = csv.DictReader(file)
            # fieldnames = ["riddles", "jokes"]

            # writer = csv.DictWriter(file, fieldnames=fieldnames)

            for line in csv_reader:
                column.append(line['riddles'])
            cowsay.fox(choice(column))

        elif user_ans == "1":

            print("Lets hear some jokes then")
            csv_reader = csv.DictReader(file)

            for line in csv_reader:
                column.append(line[1])
            cowsay.fox(choice(column))

        else:
            raise ValueError

def write_data():
    ...


if __name__ == "__main__":
    main()
