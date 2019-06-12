print(" TASK 1 : 14 lines \n")
"""
Task 1 – Auction set up.
    For every item in the auction the item number, description and the reserve price should be recorded.
    The number of bids is set to zero. There must be at least 10 items in the auction
"""


# Setting Up Items


# Number Of Bids For Item, Item Number [0->len] (Primary Key), Item Bids, Item Name, Reserve/Max Bid
noBids, itNumb, itBids, itDesc, resBid, soldIt = [], [], [], [], [], []

sumItem = 0
while sumItem < 3:     # 3 For Testing
    sumItem = int(input("How Many Items? (>=10)"))

for i in range(0, sumItem):
    print("Input Description For Item %s: " %(i+1), end="")
    idesc = input()                                                 # String Input For Item Name

    print("Input Reserve Bid: ",end="")
    iMaxBid = int(input())                                          # Integer Input For Max Bid

    itNumb.append(i+1)                                              # Primary Key of All Itams
    noBids.append(0)                                                # Number Of Bids For Item (0, default)
    itDesc.append(idesc)                                            # Append idesc (String Input For Item Name)
    resBid.append(iMaxBid)                                          # Append iMaxBid (Int Input For Max Bid)
    itBids.append([000,0])                                          # Current Top Bid,
    soldIt.append(0)








print("TASK 2: 17 LINES \n")
"""
Task 2 – Buyer bids.
A buyer should be able to find an item and view the item number, description and the current highest
bid. A buyer can then enter their buyer number and bid, which must be higher than any previously
recorded bids. Every time a new bid is recorded the number of bids for that item is increased by one.
Buyers can bid for an item many times and they can bid for many items.
"""

yesBid = True
while yesBid:           # While Loop Till User Does Not Wan't To Bid Further

    for i in range(len(itNumb)):
        print("Item Number: "+ str(itNumb[i])+" Item Name: "+ itDesc[i]+" Top Bid: "+ str(itBids[i][1]))

    reqNum = (int(input("Enter Item Number (0 is to cancel) : "))) - 1
    if reqNum == -1:
        break
    else:
        noBids[reqNum] += 1

    bidderNum = int(input("Bidder Number: "))
    bidderBid = int(input("Bid: "))

    itBids[reqNum][0] = bidderNum
    if bidderBid> itBids[reqNum][1]:
        itBids[reqNum][1] = bidderBid
    else: print("Bid For Item", str(itDesc[reqNum]),"Must Be Higher Than", str(itBids[reqNum][1]))

    if itBids[reqNum][1] >= resBid[reqNum]:
        print("Reserve Price Hit For %s" % (itNumb[reqNum]))





print("TASK 3: 17 LINES \n")
"""
Using the results from TASK 2, identify items that have reached their reserve price, mark them as sold,
calculate 10% of the final bid as the auction company fee and add this to the total fee for all sold items.
Display this total fee. Display the item number and final bid for all the items with bids that have not
reached their reserve price. Display the item number of any items that have received no bids. Display
the number of items sold, the number of items that did not meet the reserve price and the number of items with no bids.
"""

noSold, noRes, noBid = 0, 0, 0        # Number Of Sold Items / Items That Were Underbid / Items Without A Bid
itSold = []
for i in range(len(itNumb)):
    if itBids[i][1] >= resBid[i]:   # Met Reserve Bid
        noSold += 1            # Increment Items Sold,
        itSold.append(1)            # Mark Item As Sold

        finPrice = int(itBids[i][1]) * 1.1
        print(itDesc[i] + " SOLD!: To " + str(itBids[i][0]))
        print("Item No: " + str(itNumb[i]) + " Sold at " + str(itBids[i][1]) + " Final Price " + str(finPrice))

    elif itBids[i][1] == 0:         # No Bid
        noBid+= 1            # Increment Items With No Bid
        itSold.append(0)            # Mark Item As Unsold

        print("Item Number " + str(itNumb[i]) + " Received No Bids")

    else:                           # Did Not Meet Reserve Price
        noRes += 1           # Increment Items With No Bid
        itSold.append(0)            # Mark Item As Unsold
        print("Item Number " + str(itNumb[i]) + " Got A Final Bid Of" + str(itBids[i][1]))

print("Items Sold: " + str(noSold), "\nItems Didn't Sell: " + str(noRes), "\nItems Without Bid: " + str(noBid))