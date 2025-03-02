import crypto

coins = []





 ### main loop ###


what_to_do = input("What do you want to do? View holdings (1) or add more coins (2): ")



if what_to_do == "1":
    crypto.retreive_holdings(coins)
elif what_to_do == "2":
    coins = crypto.coin_holdings()









#coins = crypto.coin_holdings()