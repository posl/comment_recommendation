def is_palindrome(s):
    return s == s[::-1]
N = input()
print("Yes" if is_palindrome(N) else "No")
