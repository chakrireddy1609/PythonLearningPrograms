len = int(input("Count of numbers for which average is needed : "))

numbers = []

for i in range(0,len):
    element = int(input("Enter number : "))
    numbers.append(element)

total = sum(numbers)
average = total/len
print("Average of the numbers is : ",average)
