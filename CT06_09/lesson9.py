#import random
#num1=random.randint(1,6)
#print("First number:",num1)
#num2=random.randint(1,6)
#print("Second number:",num2)
#num3=random.randint(1,6)
#print("Third number:",num3)
#all_even_odd=(num1%2==0) == (num2%2==0) == (num3%2==0)
#print("all numbers are even/odd:",all_even_odd)

apple_cost=1
num_apples=int(input("how many apples would you like to buy?"))
if num_apples>10:
    print("Wow!That's a lot of apples!You can get a 10% discount for that!The price is"+num_apples*1*(100%-10%))
else:
    print("ok.the price is"+ "$" +(num_apples))

apple_cost=0.60
orange_cost=0.90
num_apples=int(input("how many apples would you like to buy?"))
if num_apples>5:
    print("Wow!That's a lot of apples!You can get a 10% discount for that!The price is"+num_apples*1*(100%-10%))
else:
    print("ok.the price is"+ "$" +(num_apples))
if num_oranges>5:
    print("Wow!That's a lot of oranges!You can get a 10% discount for that!The price is"+num_oranges*1*(100%-10%))
else:
    print("ok.the price is"+ "$" +(num_oranges))