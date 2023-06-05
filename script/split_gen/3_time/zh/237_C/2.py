def is_palindrome(s):
    return s == s[::-1]
s = input()
for i in range(len(s)+1):
    if is_palindrome(s[:i]+s):
        print('Yes')
        exit()
print('No')
