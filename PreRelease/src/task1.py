# Setting Up Items
"""
Task 1 – Auction set up.
    For every item in the auction the item number, description and the reserve price should be recorded.
    The number of bids is set to zero. There must be at least 10 items in the auction
"""
noBids = []
itNumb = []
itBids = []
itDesc = []
resBid = []
inStat = []

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
    iminbid = int(input())

    itNumb.append(i+1)
    noBids.append(0)
    itDesc.append(idesc)
    resBid.append(iminbid)
    itBids.append(["000",0])

inStat = [itNumb,noBids,itDesc,resBid,itBids]


