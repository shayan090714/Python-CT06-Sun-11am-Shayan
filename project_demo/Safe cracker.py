import random
num1 = random.randint(0,4)
print(num1)
num2 = random.randint(5,10)
print(num2)
num3 = random.randint(0,10)
print(num3)
chances = 3
print("This is a safe.For each digit,you have 3 chances to figure out the number.Else,the safe will auto lock.")
while not chances == 0:
    ans1 = (int(input("!The first number is between 0 and 4.What is the first number?")))
    if ans1 == num1:
        chances = 3
        ans2 = (int(input("Correct!The second number is between 5 and 10.What is the second number?")))
        if ans2 == num2:
            chances = 3
            ans3 = (int(input("Correct!The third number is between 0 and 10.What is the third number?")))
            if ans3 == num3:
                print("You have unlocked the safe!")
                break
            else:
                chances = chances-1
                print("Wrong!The amount of chances you have left is",chances,".")
                ans3 = (int(input("What is the number?")))
        else:
            chances = chances-1
            print("Wrong!The amount of chances you have left is",chances,".")
            ans2 = (int(input("What is the number?")))
    else:
        chances = chances-1
        print("Wrong!The amount of chances you have left is",chances,".")
        ans1 = (int(input("What is the number?")))
print("Safe is locked.")
