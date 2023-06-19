def count(s, num):
    cnt = 0
    for i in range(4):
        if s[i] == 'o' and num[i] == '0':
            return 0
        if s[i] == 'x' and num[i] == '1':
            return 0
        if s[i] == '?' and num[i] == '0':
            return 0
        if s[i] == '?' and num[i] == '1':
            return 0
        if s[i] == '?' and num[i] == '?':
            cnt += 1
    return 2 ** cnt
s = input()
ans = 0
for i in range(10000):
    num = str(i).zfill(4)
    ans += count(s, num)
print(ans)
