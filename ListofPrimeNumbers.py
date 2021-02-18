user_input = int(input("Enter a number to check the list of prime numbers less than it : "))


def all_primes(number):


    prime = []
    for i in range(2,number):
        for j in range(2,number):
            if i != j:
                if i % j == 0:
                    break;
                else:
                    continue;
            else:
                prime.append(i)
    print(prime)


all_primes(user_input)



