def is_palindrome(s):
    return s == s[::-1]
s = input()
for i in range(len(s)):
    s2 = 'a'*i + s
    if is_palindrome(s2):
        print('Yes')
        exit()
print('No')

if __name__ == '__main__':
    is_palindrome()