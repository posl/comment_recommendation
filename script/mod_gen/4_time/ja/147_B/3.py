def is_palindrome(s):
    return s == s[::-1]
s = input()
n = len(s)
ans = 0
for i in range(n//2):
    if s[i] != s[-1-i]:
        ans += 1
print(ans)

if __name__ == '__main__':
    is_palindrome()