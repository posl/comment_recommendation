def judge(s):
    for i in range(1, len(s)):
        if s == s[i:] + s[:i]:
            return True
    return False
n = int(input())
s = input()
print("Yes" if judge(s) else "No")
