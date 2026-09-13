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
