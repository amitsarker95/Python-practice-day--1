number = int(input("Enter The number : "))
reversedNumber = 0
while number!=0:
    last_digit = number % 10
    reversedNumber = reversedNumber * 10 + last_digit
    number //= 10

print(reversedNumber)
