# Done by Stephen N.
b = int(input())
p = 5*b - 400
boil = 100

if p < 100:
    boil = 1
elif p > 100:
    boil = -1
else:
    boil = 0

print(p)
print(boil)