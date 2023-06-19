def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i <= j:
        if s[i] != s[j]:
            return False
        i = i + 1
        j = j - 1
    return True
s = input()
n = len(s)
for i in range(n + 1):
    t = 'a' * i + s
    if is_palindrome(t):
        print('Yes')
        exit()
print('No')

if __name__ == '__main__':
    is_palindrome()