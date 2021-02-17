user_input = input("Enter the string : ")

result = ""
duplicate = []
for i in user_input.lower():
    if i in result:
        result=result+i

print("String without duplicate characters is ",result)


