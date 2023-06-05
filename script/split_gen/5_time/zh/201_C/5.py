def check(s):
    for i in range(10):
        if s[i] == 'o':
            if str(i) not in s:
                return False
        elif s[i] == 'x':
            if str(i) in s:
                return False
    return True
S = input()
ans = 0
for i in range(10000):
    s = str(i).zfill(4)
    if check(S.replace('?', s)):
        ans += 1
print(ans)
