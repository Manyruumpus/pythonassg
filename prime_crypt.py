import math

def nprimesum(n):
    if n < 1:
        raise ValueError("input must be a positive number!")  # Still keeping this guard in place

    # For small numbers, just go with a safe limit
    if n < 6:
        uplim = 15
    else:
        # formula from some forum – might revisit later
        uplim = int(n * (math.log(n) + math.log(math.log(n)))) + 5

    while True:
        #  the sieve method
        isprime = [True] * (uplim + 1)
        isprime[0] = False
        isprime[1] = False

        prime_list = []

        # Basic Sieve of Eratosthenes
        for num in range(2, uplim + 1):
            if isprime[num]:
                prime_list.append(num)

                # remove all multiples
                for factor in range(num*num, uplim + 1, num):
                    isprime[factor] = False

                # No need to keep going if we got 
                if len(prime_list) >= n:
                    break

        if len(prime_list) >= n:
            # Summing up the first n primes 
            total_sum = 0
            for idx in range(n):
                total_sum += prime_list[idx]
            return total_sum

        # If we didn’t find enough primes, just try a bigger limit
        uplim *= 2  # brute force


#  Main bit starts 

p = input("Enter a number: ")

try:
    p_num = int(p)
except:
    print("Please enter a valid integer.")
    quit()

ans= nprimesum(p_num)

print("SUM OF FIRST " + p +  " PRIME NUMBERS IS:", end = " ")
print(ans)
