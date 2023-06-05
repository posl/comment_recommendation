def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
s = input()
for i in range(len(s)+1):
    s1 = s[:i] + 'a' + s[i:]
    if is_palindrome(s1):
        print('Yes')
        exit()
print('No')

if __name__ == '__main__':
    is_palindrome()