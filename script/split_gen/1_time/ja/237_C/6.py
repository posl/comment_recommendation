def is_palindrome(s):
    return s == s[::-1]
s = input()
cnt = 0
while True:
    if is_palindrome(s):
        break
    s = "a" + s
    cnt += 1
print("Yes" if cnt else "No")
