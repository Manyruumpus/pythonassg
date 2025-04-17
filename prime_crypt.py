import math

def prime_n_sum(n):
    if n < 1:
        raise ValueError("Input must be a positive number!")
    if n < 6:
        limit = 15
    else:
        # rough estimate of the nth prime
        limit = int(n * (math.log(n) + math.log(math.log(n)))) + 5

    while True:
        # mark primes using a simple boolean array
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False  # Not primes

        primes = []

        for num in range(2, limit + 1):
            if sieve[num]:
                primes.append(num)

                # cross out all multiples of this prime
                for j in range(num * num, limit + 1, num):
                    sieve[j] = False

                if len(primes) >= n:
                    break  
        if len(primes) >= n:
            total = 0
            for i in range(n):
                total += primes[i]
            return total  

        limit *= 2

n = input("Enter a number: ")
ans = prime_n_sum(int(n))
print("SUM OF FIRST " + n +  " PRIME NUMBERS IS:", end = " ")
print (ans)