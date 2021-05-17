number = int(input("Enter the number : "))

sum_of_cubes = 0

if number > 1:
    for i in range(1,number+1):
        sum_of_cubes = sum_of_cubes + (i*i*i)
    print(sum_of_cubes)
else:
    print("Input number is invalid")

