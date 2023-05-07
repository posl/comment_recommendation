def is_palindrome(s):
    return s == s[::-1]
s = input()
ans = 0
while not is_palindrome(s):
    s = s[:-1]
    ans += 1
print(ans)

if __name__ == '__main__':
    is_palindrome()