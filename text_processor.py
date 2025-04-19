# inputs 
n = input("Enter the reg no.: ")
s = input("Enter the string (containing only letters): ")

#  validate inputs 
try:
    num = int(n)
    if num <= 0:
        print("invalid reg number, it should be positive")
        quit()
except:
    print("invalid registration number, it should be an integer.")
    quit() 
# string – should only be letters
if not s.isalpha():
    print("Invalid string.")
    quit()

#  process string on whether num is odd or even
# if even:reverse 
if num % 2 == 0:
    result_s = s[::-1]
else:
    # odd:transform vowels to uppercase ans so
    vowels = "aeiouAEIOU"
    chars = []
    for ch in s:
        if ch in vowels:
            chars.append(ch.upper())
        else:
            chars.append(ch.lower())
    result_s = ''.join(chars)  # rebuild the string

#  number of 1 in num binary
bit1 = bin(num).count('1')

#  all substrings of length bit count 

substr = []
# if the count is not zero
if bit1 > 0:
    for idx in range(len(result_s) - bit1 + 1):
        piece = result_s[idx:idx+bit1]
        substr.append(piece)
# else: don't do anything

#  sorting or reversing 
if (num & len(s)) == 0:
    substr.sort()  # simple sort
else:
    substr = substr[::-1]  # flipping the list entirely

# final output 

print("Output:")
print(' '.join(substr))  # Output all substrings space-separated
