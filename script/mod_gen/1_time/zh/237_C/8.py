def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
S = input()
for i in range(len(S)+1):
    s = 'a' * i + S
    if is_palindrome(s):
        print('Yes')
        exit()
print('No')

if __name__ == '__main__':
    is_palindrome()