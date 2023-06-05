def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
s = input()
n = len(s)
cnt = 0
for i in range(n//2):
    if s[i] != s[n-i-1]:
        cnt += 1
print(cnt)

if __name__ == '__main__':
    is_palindrome()