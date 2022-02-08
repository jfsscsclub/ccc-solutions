# Done by Aritro S.
mySum = 0
prevInstruction = ""

while True:
    instruction = input()

    if instruction == "99999":
        break
    
    mySum = int(instruction[0]) + int(instruction[1])
    steps = int(instruction[2:])

    if mySum == 0:
        print(f"{prevInstruction} {steps}")
    elif mySum % 2 == 0:
        print(f"right {steps}")
        prevInstruction = "right"
    else:
        print(f"left {steps}")
        prevInstruction = "left"