def isPalindrome(s):
    n = len(s)
    if n == 1:
        return True
    if n == 2:
        return s[0] == s[1]
    if n%2 == 0:
        return False
    if s[0] != s[-1]:
        return False
    return isPalindrome(s[1:-1])
s = input()
n = len(s)
s1 = s[0:(n-1)//2]
s2 = s[(n+1)//2:]
print('Yes' if isPalindrome(s) and isPalindrome(s1) and isPalindrome(s2) else 'No')

if __name__ == '__main__':
    isPalindrome()