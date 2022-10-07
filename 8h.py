def isPrime(x):
    isFound = True
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                isFound = False
                break
    return isFound


l = int(input("Enter start : "))
r = int(input("Enter End : "))

for k in range(l,r):
    if isPrime(k) == True:
        print(k)
print()

