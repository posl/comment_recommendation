def is_palindrome(word):
    return word == word[::-1]
S = input()
count = 0
while not is_palindrome(S):
    S = S[0:-1]
    count += 1
print(count)
