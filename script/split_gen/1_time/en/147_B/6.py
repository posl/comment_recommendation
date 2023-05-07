def isPalindromic(s):
    return s == s[::-1]
s = input()
count = 0
while not isPalindromic(s):
    count += 1
    s = s[:-1]
print(count)
