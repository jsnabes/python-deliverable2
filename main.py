cart = []
price = []
items = ["apple", "grape", "orange"]
user_name = input("Welcome to the GC Fruit Market! What is your name? ")
menu = ["Apple $2", "Grape $1", "Orange $3"]
print("                ")
print(f"Welcome {user_name}. Which fruit would you like to buy?")
print(f"1. {menu[0]}")
print(f"2. {menu [1]}")
print(f"3. {menu[2]}")
fruit_number = int(input("> "))
if fruit_number == 1:
    price.append(2)
    cart.append(items[0])
    print("You bought 1 apple at $2")
elif fruit_number == 2:
    price.append(1)
    cart.append(items[1])
    print("You bought 1 grape at $1")
elif fruit_number == 3:
    price.append(3)
    cart.append(items[2])
    print("You bought 1 orange at $3")
ask_again = input("Would you like to buy another piece of fruit? y/n ")
if ask_again == "n":
    print("  ")
    print(f"Order summary for {user_name}")
    count = cart.count("apple")
    print(count, "apple(s) at $2 each")
    count2 = cart.count("grape")
    print(count2, "grape(2) at $1 each")
    count3 = cart.count("orange")
    print(count3, "orange(s) at $3 each")
    total_price = sum(price)
    print(f"Sub Total: ${total_price}")
    print(f"5% Tax: ${total_price *0.05}")
    grand_total = total_price + total_price * 0.05
    print(f"Total: ${grand_total}")

while ask_again == "y":
    print(f"Welcome {user_name}. Which fruit would you like to buy?")
    print(f"1. {menu[0]}")
    print(f"2. {menu[1]}")
    print(f"3. {menu[2]}")
    more_fruit = int(input("> "))
    if more_fruit == 1:
        price.append(2)
        cart.append(items[0])
        print("You bought 1 apple at $2")
    elif more_fruit == 2:
        price.append(1)
        cart.append(items[1])
        print("You bought 1 grape at $1")
    elif more_fruit == 3:
        price.append(3)
        cart.append(items[2])
        print("You bought 1 orange at $3")
    final_ask = input("Would you like to buy another piece of fruit? y/n ")
    if final_ask == "n":
        print("   ")
        print(f"Order summary for {user_name}")
        count = cart.count("apple")
        print(count, "apple(s) at $2 each")
        count2 = cart.count("grape")
        print(count2, "grape(s) at $1 each")
        count3 = cart.count("orange")
        print(count3, "orange(s) at $3 each")
        total_price = sum(price)
        print(f"Sub Total: ${total_price}")
        print(f"5% Tax: ${total_price * 0.05}")
        grand_total = total_price + total_price * 0.05
        print(f"Total: ${grand_total}")
        break
