def f(s):
    n = len(s)
    ans = 0
    for i in range(n):
        ans = ans * 26 + ord(s[i]) - ord('A') + 1
    return ans
s = input()
print(f(s))
