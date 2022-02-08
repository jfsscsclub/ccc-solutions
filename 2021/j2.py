# Done by Stephen N.
n = int(input())
topBidder = ""
topBid = -100

for i in range(n):
  bidder = input()
  bid = int(input())
  if bid > topBid:
    topBid = bid
    topBidder = bidder
  
print(topBidder)