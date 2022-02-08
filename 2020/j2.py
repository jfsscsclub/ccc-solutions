# Done by Stephen N.
p = int(input())
n = int(input())
r = int(input())

days = 0
infected = n
infectedYesterday = n

while infected <= p:
  infectedYesterday *= r
  infected += infectedYesterday
  days += 1

print(days)
