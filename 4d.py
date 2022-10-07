str = input("Enter a string : ")
lowerCase = 0
upperCase = 0
digits = 0
symbols = 0

for i in str:
    acci = ord(i)
    if (acci >= 97) and (acci <= 122) :
        lowerCase+=1
    elif (acci >= 65) and (acci <= 90) :
        upperCase+=1
    elif(acci >= 48) and (acci <= 57) :
        digits+=1
    else:
        symbols+=1
    
print(f"Uppercase : {upperCase}")
print(f"Lowercase : {lowerCase}")
print(f"Digits : {digits}")
print(f"Symbols : {symbols}")

# P@#yn26at^&i5ve
