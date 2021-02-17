user_input = input("Enter the string : ")

result = ""
for i in user_input.lower():
    if i not in result:
        result = result+i

print("String without duplicate characters is ", result)


