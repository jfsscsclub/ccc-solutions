# Done by Stephen N.
n = int(input())

xCoords = []
yCoords = []

for i in range(n):
  xy = input().split(",")
  x = int(xy[0])
  y = int(xy[1])
  xCoords.append(x)
  yCoords.append(y)

xCoords.sort()
yCoords.sort()

print(str(xCoords[0]-1) + "," + str(yCoords[0]-1))
print(str(xCoords[n-1]+1) + "," + str(yCoords[n-1]+1))