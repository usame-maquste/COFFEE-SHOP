#We Are F-Society !!

print("Hello, Welcome to HURBAD Coffee Shop  !!!\n")

name = input("What is your name ?\n")

print ("Hello "+ name +" , Thank you  so much for coming in today.\n")

menu = "Black Coffee, Espresso, Latte Cappucino, Macchiato"

print(name + ", What would you like from our menu today ? Here is what we are serving. .\n"+menu)

order = input()

price = 5

quantity = input("How many coffees would you like ?\n")

total = price * int(quantity)


print("Thank you , Your total is: $" + str(total))


print("Okey-dokey " + name + ", We'll have your " + quantity + " " + order + " ready for you in a moment.")
