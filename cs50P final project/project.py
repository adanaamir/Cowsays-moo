import cowsay, csv
from random import choice
import sys

def main():
    user_answer = user_choice()
    read_data(user_answer)

def user_choice():
    ans = input("Are you feeling lazy and need motivation or maybe hear a joke? (yes/yepp) ").strip().lower()
    while True:
        if ans[0] == "y":
            advice = input("Cool! Do you need me to motivate you or tell you a joke? (0 = motivate / 1= joke) ").lower()
            return advice   #this ends the loop after user gives a response
        else:
            ans = input("I dont take that response, you have to say yes :( ").lower()
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
    list = []
    with open("fortunes.csv", "r", newline= '') as file:
        if user_ans == "0":
            response = input("aww cmon lets hear some jokes instead? (okay/nah) ")

            if response in ["okay", "alright", "ok"]:
                print("YIPIEES!\n Here's a joke for you:")
                csv_reader = csv.reader(file)

                for line in csv_reader:
                    list.append(line[1]) 
                cowsay.fox(choice(list))

            elif response[0] == "n":
                print("Alright then! lets get you a motivational quote")
            # while True:
            csv_reader = csv.reader(file)

            for line in csv_reader:
                list.append(line[0])  #appending the first column(motivational quotes) to the list
            cowsay.cow(choice(list))
                    # response_2 = input("Do you wanna hear another one? (y/n) ")

        elif user_ans == "1":
            csv_reader = csv.reader(file)

            for line in csv_reader:
                list.append(line[1])
            cowsay.fox(choice(list))

def write_data():
    ...


if __name__ == "__main__":
    main()
