import crypto

coins = []
price = 0
name = ""
ammount = 0








 ### main loop ###
while True:
    name = input("\nEnter the name of the coin: ")
    price = input("\nEnter the price of the coin: ")
    ammount = input("\nEnter the ammount of the coin: ")
    coins.append(crypto.Crypto(name, price, ammount))
    if input("Do you want to add another coin? (y/n): ") == "n":
        break
