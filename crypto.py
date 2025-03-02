


def coin_holdings():
    coins = []
    while True:
        name = input("\nEnter the name of the coin: ")
        try:
            price = int(input("\nEnter the price of the coin: "))
            ammount = input("\nEnter the ammount of the coin: ")
        except ValueError:
            print("Please enter a number \n")
            value_error = True
        if input("Do you want to save?, (y/n): ") == "n" and value_error == False:
            break
        if value_error == False:
            coins.append((name, price, ammount))
        if input("Do you want to add another coin? (y/n): ") == "n":
            break
    
    return coins



def retreive_holdings(coins):
    for coin in coins:
        print("\nCoin:" + str(coin[0]) + "\nPrice:"+ str(coin[1]) + "\nAmmount: " + str(coin[2]) +"\n")

    print("all coin in wallet printed")

