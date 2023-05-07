def is_palindrome(s):
    return s == s[::-1]
s = input()
ans = 0
for i in range(len(s)):
    if not is_palindrome(s):
        ans += 1
        s = s[:-1]
    else:
        break
print(ans)
