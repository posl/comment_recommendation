def is_palindrome(s):
    return s == s[::-1]
N = input()
for i in range(10):
    if is_palindrome('0'*i + N):
        print('Yes')
        exit()
print('No')
