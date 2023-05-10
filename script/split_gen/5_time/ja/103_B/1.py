def rotate(s):
    return s[1:] + s[0]
s = input()
t = input()
ans = "No"
for i in range(len(s)):
    if s == t:
        ans = "Yes"
        break
    s = rotate(s)
print(ans)
