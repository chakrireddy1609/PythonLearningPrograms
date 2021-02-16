number = int(input("Enter a number : "))

list_of_nums = []
for i in range(number):
    if i%2==0 and i%3==0:
        list_of_nums.append(i)

print(list_of_nums)