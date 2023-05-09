def isPalindrome(s):
    n = len(s)
    for i in range(n):
        if s[i] != s[n-1-i]:
            return False
    return True
s = input()
n = len(s)
for i in range(n):
    if isPalindrome(s[i:]):
        print("Yes")
        exit()
print("No")
