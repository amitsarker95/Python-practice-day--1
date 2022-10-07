str = input("Enter a string : ")
result = ""
for i in str :
    k = ord(i)
    if (k >= 97) and (k <= 122) :
        result += chr(k-32)
    elif (k >= 65) and (k <= 90) :
        result += chr(k+32)
    else :
        result+=i

print(result)