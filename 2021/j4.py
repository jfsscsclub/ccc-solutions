# Done by Aritro S.
shelf = input()

numberOfL = shelf.count("L")
numberOfM = shelf.count("M")
numberOfS = shelf.count("S")

# Use list slicing to get each section
sectionL = shelf[0 : numberOfL]
sectionM = shelf[numberOfL : numberOfL + numberOfM]
sectionS = shelf[numberOfL + numberOfM:]

# Count the amount of swaps needed per each section
lSwaps = sectionL.count("M") + sectionL.count("S")
mSwaps = sectionM.count("L") + sectionM.count("S")

finalAns = lSwaps + mSwaps - min(sectionM.count("L"), sectionL.count("M"))

print(finalAns)