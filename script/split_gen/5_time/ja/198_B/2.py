def isPalindrome(s):
    return s == s[::-1]
n = input()
print("Yes" if isPalindrome(n) else "No")
