cart = []
item_price = []

user_name = input("Welcome to the GC Fruit Market! What is your name? ")
menu = ["Apple $2", "Grape $1", "Orange $3"]
print("                ")
print(f"Welcome {user_name}. Which fruit would you like to buy?")
print(f"1. {menu[0]}")
print(f"2. {menu [1]}")
print(f"3. {menu[2]}")
fruit_number = int(input("> "))
if fruit_number == 1:
    cost = 2
    print("You bought 1 apple at $2")
elif fruit_number == 2:
    cost = 1
    print("You bought 1 grape at $1")
elif fruit_number == 3:
    cost = 3
    print("You bought 1 orange at $3")
ask_again = input("Would you like to buy another piece of fruit? y/n ")
while ask_again == "y":
    print(f"Welcome {user_name}. Which fruit would you like to buy?")
    print(f"1. {menu[0]}")
    print(f"2. {menu[1]}")
    print(f"3. {menu[2]}")
    more_fruit = int(input("> "))
    if more_fruit == 1:
        cost = 2
        print("You bought 1 apple at $2")
    elif more_fruit == 2:
        cost = 1
        print("You bought 1 grape at $1")
    elif more_fruit == 3:
        cost = 3
        print("You bought 1 orange at $3")
    final_ask = input("Would you like to buy another piece of fruit? y/n ")
else:
    print(f"Receipt for {user_name}")

