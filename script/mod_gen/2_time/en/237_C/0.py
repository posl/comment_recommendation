def is_palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True
s = input()
for i in range(len(s)):
    if is_palindrome(s[i:]+s[:i]):
        print('Yes')
        exit(0)
print('No')

if __name__ == '__main__':
    is_palindrome()