"""
Task 2 – Buyer bids.
A buyer should be able to find an item and view the item number, description and the current highest
bid. A buyer can then enter their buyer number and bid, which must be higher than any previously
recorded bids. Every time a new bid is recorded the number of bids for that item is increased by one.
Buyers can bid for an item many times and they can bid for many items.
"""

import task1

resBid = task1.resBid
itDesc = task1.itDesc
itNumb = task1.itNumb
itBids = task1.itBids
noBids = task1.noBids
inStat = task1.inStat

yesBid = True
whoBid = []


while yesBid:
    yesBid = bool(input("Click Enter To Quit / Any Key To Continue: "))
    if not yesBid:
        break

    while True:
        try:
            reqNum = int(input("Enter Item Number: "))
        except ValueError:
            print("ValueError, retry")
            continue
        except IndexError:
            print("IndexError, retry")
            continue
        except TypeError:
            print("TypeError, retry")
            continue
        else:
            if reqNum>task1.sumItem:
                print("Out of range")
                continue

            break

    # print("Highest Bid For Item %s Is: %i" %(str(itDesc[reqNum]), int(resBid[reqNum][1]))). BoardWorks organic

    while True:
        try:
            resBid[reqNum] = int(input("Buyer Number: "))
            preBid = int(input("Bid For Item: "))
        except ValueError:
            print("ValueError, retry")
            continue
        except IndexError:
            print("IndexError, retry")
            continue
        except TypeError:
            print("TypeError, retry")
            continue
        else:
                itBids[reqNum][0] = 0
                itBids[reqNum][1] = preBid
                noBids[reqNum] += 1
                break




