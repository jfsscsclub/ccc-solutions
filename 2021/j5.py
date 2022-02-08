# Done by Stephen N.
m = int(input())
n = int(input())
k = int(input())

rowNum = 0
colNum = 0
paintDict = {}

for i in range(k):
  paintCurrent = input()

  if paintCurrent in paintDict:
    del paintDict[paintCurrent]
  else:
    paintDict[paintCurrent] = paintCurrent[0]

for i in paintDict:
  if paintDict[i] == "R":
    rowNum += 1
  else:
    colNum += 1

overlap = rowNum*colNum*2
output = rowNum*n + colNum*m - overlap
print(output)