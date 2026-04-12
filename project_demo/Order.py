final_order = ""
reply = input("What would you like to order")
while not reply == "end":
    final_order = final_order + "," + reply
    reply = input("What would you like to order")
print("Your order",final_order)