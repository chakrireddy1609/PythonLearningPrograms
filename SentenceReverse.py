sentence = input("Enter sentence : ")

words = sentence.split()
words.reverse()
reverse_sentence = " ".join(words)
print(reverse_sentence)