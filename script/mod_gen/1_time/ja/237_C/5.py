def is_palindrome(s):
    return s == s[::-1]
s = input()
n = len(s)
for i in range(n):
    t = s + 'a' * i
    if is_palindrome(t):
        print('Yes')
        exit()
print('No')

if __name__ == '__main__':
    is_palindrome()