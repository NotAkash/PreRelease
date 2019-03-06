# Setting Up Items
"""
Task 1 – Auction set up.
    For every item in the auction the item number, description and the reserve price should be recorded.
    The number of bids is set to zero. There must be at least 10 items in the auction
"""
noBids = []             # Number Of Bids
itNumb = []             # Item Number [0->len]
itBids = []             # Item Bids [0->resBid]     
itDesc = []             # Item Name
resBid = []             # Reserve Bid [Max Bid Price]

while True:
    try:
        sumItem = int(input("How Many Items? (>=10)"))
    except TypeError:
        continue
    except ValueError:
        continue
    else:
        if sumItem <3:
            print(">=10")
            continue
        else:
            break
            
for i in range(0, sumItem):
    print("Input Description For Item %s: " %(i+1), end="")
    idesc = input()
    print("Input Reserve Bid: ",end="")
    iMaxBid = int(input())

    itNumb.append(i+1)
    noBids.append(0)
    itDesc.append(idesc)
    resBid.append(iMaxBid)
    itBids.append([000,0])

inStat = [itNumb,noBids,itDesc,resBid,itBids]


