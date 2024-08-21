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
            # with open("before.csv", "w") as new_file:
            #     fieldnames = ["answers"]
            #     writer = csv.DictWriter(new_file, fieldnames=fieldnames)

            #     writer.writeheader()
            #     for line in writer:
            #         writer.writerow(answer)

            for line in csv_reader:
                ans.append(line['answers'])
            
            for i in ans:
                if answer == ans[i]:
                    print("Correct")
                else:
                    print("Nope try again")


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
