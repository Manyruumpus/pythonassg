n_input = input("Enter the registration number: ")
s = input("Enter the string (containing only letters): ")

# 2. Validate input
try:
    n = int(n_input)
    if n <= 0:
        print("REGISTRATION NUMBER MUST BE A POSITIVE INTEGER")
        quit()
except ValueError:
    print("Invalid registration number. Must be an integer.")
    quit()

if not s.isalpha():
    print("STRING MUST CONTAIN ONLY LETTERS")
    quit()

if n % 2 == 0:
    processed = s[::-1]
else:
    vowels = "aeiouAEIOU"
    processed = ''.join(
        ch.upper() if ch in vowels else ch.lower()
        for ch in s
    )

k = bin(n).count('1')

# 5. Part 3 – extract_substrings of length k
substrings = []
# if k is 0 (possible only if n==0, but we've ruled that out), we’d skip.
for i in range(len(processed) - k + 1):
    substrings.append(processed[i:i+k])

# 6. Part 4 – sort_or_reverse based on (n & len(s)) == 0
if (n & len(s)) == 0:
    substrings.sort()
else:
    substrings.reverse()

# 7. Output
print("Output:")
print(' '.join(substrings))
