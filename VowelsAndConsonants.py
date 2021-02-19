vowels = ['a', 'e', 'i', 'o', 'u']
user_string = input("Enter a string : ")

vowels_count = 0
consonants_count = 0

for char in user_string.lower():
    if char in vowels:
        vowels_count += 1
    else:
        consonants_count += 1

print("Count of vowels is ", vowels_count)
print("Count of consonants is ", consonants_count)

