import os
from dotenv import load_dotenv


load_dotenv()
admin_password = os.getenv("calculator_ADMIN_PASSWORD")

open_admin = input("do u want to open admin mode?   yes/no:  ")

if open_admin.lower() == "yes":
    entered_password = input("enter admin password:  ")
    if entered_password == admin_password:
        print("admin! hi...")
    else:
        print("wrong password")

from question import queitions
name = input("whats your name? ")

score = 0
print("welcome")
for item in queitions:
    answer = input(item["question"])

    if answer.lower() == item["answer"]:
        print("correct")
        score += 1

    else:
        print("wrong")



print("your score is: ", score, "out of ", len(queitions))

if score == len(queitions):
    print("excellent job", name)
elif score >= 2:
    print("good job", name)

else:
    print(f"keep praticong {name}")

with open("result.txt", "a") as file:
    file.write(f"{name} - {score}/{len(queitions)}\n")
