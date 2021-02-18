number = int(input("Enter a number : "))

reverse = 0
while number>0:
    first_digit = number%10
    reverse = reverse * 10 + first_digit
    number = number//10
print(reverse)


