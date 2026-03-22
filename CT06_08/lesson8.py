#total=0
#for count in range(1,5+1):
    #answer=input("give me a number #"+ str(count))
    #total=total+int(answer)
#print("average=",total/5)

#total=0
#for count in range(1,5+1):
    #answer=input("give me a number #"+ str(count))
    #total=total+int(answer)
#print("answer=",total*5)

#import time
#for i in range(10,0,-1):
    #print(i)
    #time.sleep(1)
#print("Liftoff!")

#import random
#num=random.randint(1,6)
#print(num)

#import random
#for count in range(20):
    #num=random.randint(0,9999)
    #print(num)

#isholiday=True
#isfun=True
#islong=True
#x="5"
#y="five"
#print(not isfun)
#print (x==y)

import random
num_questions=int(input("How many questions?"))
for count in range(num_questions):
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    question="What is"+str(num1)+"+"+str(num2)+"?"
    hidden_answer=num1+num2
    user_answer = int(input(question))
    if hidden_answer == user_answer:
        print("correct")
    else:
        print("wrong")


