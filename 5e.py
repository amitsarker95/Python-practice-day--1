str1 = input("Enter String 1 :")
str2 = input("Enter String 2 :")

finalStr = ""
i = -1
for x in str1:
    finalStr += x
    finalStr += str2[i]
    i -= 1
print(finalStr)