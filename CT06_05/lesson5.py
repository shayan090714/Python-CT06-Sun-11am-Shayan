print("Hello from lesson 5")
#for count in range(100):
    #print("i like chicken rice")

#for count in range(10):
    #print("I like cake. Give me more!")

#myword="Shayan"
#for letter in myword:
#    print("give me a", letter)

#print("i am", myword) 

#for count in range(5,0,-1):
    #print(count)

n1=input("give me a number:") 
n1=int(n1)
n2=input("give me another number:") 
n2=int(n2)

if n1>n2:
    start=n2
    stop=n1
else:
    start=n1
    stop=n2

for count in range(start,stop):
    print(count)