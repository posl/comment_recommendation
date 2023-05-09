def is_palindrome(s):
    return s == s[::-1]
s = input()
l = len(s)
c = 0
for i in range(l//2):
    if s[i] != s[l-i-1]:
        c += 1
print(c)

if __name__ == '__main__':
    is_palindrome()