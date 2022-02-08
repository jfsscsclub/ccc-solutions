# Done by Aritro S.
while True:
  numbers = [int(x) for x in input().split()]
  if len(numbers) == 1:
    break
  elif len(numbers) == 2:
    print(0)
  
  # Exclude n
  numbers = numbers[1:]

  # Get the differences between adjacent numbers
  differences = [numbers[x + 1] - numbers[x] for x in range(len(numbers) - 1)]

  for i in range(1, len(differences) + 1):
    isGood = True

    # First subset of differences
    subset = differences[0:i]

    # Get the amount of subsets of the differences that
    # 1. do not intersect
    # 2. have a length of i
    subsetsCount = int(len(differences) / i)

    for x in range(subsetsCount):
      if differences[i*x : i*(x+1)] != subset:
        isGood = False
        break
    
    # Don't bother with the next loop if it's already not good
    if not isGood:
      continue

    # Get the remaining differences that may have not been caught by the first loop
    if i * subsetsCount < len(differences):
      remaining = differences[i*subsetsCount:]

      for z in range(min(len(remaining), len(subset))):
        if remaining[z] != subset[z]:
          isGood = False
          break
    
    if isGood:
      print(len(subset))
      break