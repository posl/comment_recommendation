def is_palindrome(s):
    return s == s[::-1]
s = input()
for i in range(len(s)+1):
    t = s + "a" * i
    if is_palindrome(t):
        print("Yes")
        exit()
print("No")
