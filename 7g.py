number = int(input("Enter the number : "))
tmp = number
reversed_num = 0

while number != 0:
    digit = number % 10
    reversed_num = reversed_num * 10 + digit
    number //= 10

if tmp == reversed_num:
    print("True")
else :
    print("False")