# Done by Aritro S.
variables = { "A": 0, "B": 0 }
while True:
  command = input().split()
  instruction = int(command[0])

  if len(command) == 1:
    break
  elif len(command) == 2:
    varKey = command[1]
    print("Output:", variables[varKey])
  elif len(command) == 3:
    varKey = command[1]
    numOrVar = command[2]

    if instruction == 1:
      variables[varKey] = int(numOrVar)
    elif instruction == 3:
      variables[varKey] = variables[varKey] + variables[numOrVar]
    elif instruction == 4:
      variables[varKey] = variables[varKey] * variables[numOrVar]
    elif instruction == 5:
      variables[varKey] = variables[varKey] - variables[numOrVar]
    elif instruction == 6:
      variables[varKey] = int(variables[varKey] / variables[numOrVar])
