def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
s = input()
n = len(s)
for i in range(n+1):
    if is_palindrome(s[:i] + 'a' + s[i:]):
        print('Yes')
        exit()
print('No')

if __name__ == '__main__':
    is_palindrome()