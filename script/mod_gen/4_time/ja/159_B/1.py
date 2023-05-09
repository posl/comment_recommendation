def isPalindrome(s):
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            return False
    return True
s = input()
n = len(s)

if __name__ == '__main__':
    isPalindrome()