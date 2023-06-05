def is_palindrome(s):
    return s == s[::-1]
S = input()
for i in range(len(S) + 1):
    if is_palindrome("a" * i + S):
        print("Yes")
        exit()
print("No")
