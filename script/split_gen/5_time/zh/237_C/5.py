def is_palindrome(s):
    return s == s[::-1]
s = input()
ans = 'Yes' if is_palindrome(s) else 'No'
print(ans)
