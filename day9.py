
#from art import logo
#print(logo)



bidding_continues = True
bidding_list = {}

while bidding_continues:
    key = input("What is your name?: ")
    value = int(input("What is your bid?: $ "))
    bidding_list[key] = value

    bidding_status = input("Are there any other bidders? Type 'yes' or 'no'." ).lower()

    if bidding_status == "yes":
        print("\n" * 100)
    else:
        bidding_continues = False
        bid = 0
        for keys in bidding_list:
            if bidding_list[keys] > bid:
                bid = bidding_list[keys]
                winner = keys
        print(bidding_list)
        print(f"The winner is {winner} with a bid of ${bid}.")
