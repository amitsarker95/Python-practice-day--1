x = int(input("Enter a number :"))
arr = [0, 1]
i = 0
for k in range(x-2):
    result = arr[i] + arr[i+1]
    arr.append(result)
    i+=1

for z in arr:
    print(z,end=" ")