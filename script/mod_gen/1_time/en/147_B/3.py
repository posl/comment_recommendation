def is_palindrome(s):
    return s == s[::-1]
s = input()
ans = 0
for i in range(len(s)):
    if not is_palindrome(s[i:]):
        ans = len(s) - i
        break
print(ans)

if __name__ == '__main__':
    is_palindrome()