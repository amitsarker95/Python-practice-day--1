number = int(input("Enter a number : "))

for i in range(1, number+1):
    for x in range(1, i+1):
        print("*", end="")
    print()
for k in range(number-1, 0, -1):
    for z in range(k, 0, -1):
        print("*",end="")
    print()