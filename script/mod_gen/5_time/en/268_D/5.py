def check(s, t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] != '_' and t[i] != '_' and s[i] != t[i]:
            return False
    return True
n, m = map(int, input().split())
s = [input() for _ in range(n)]
t = [input() for _ in range(m)]
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if check(s[i], s[j]):
            print(-1)
            exit()
for i in range(m):
    for j in range(m):
        if i == j:
            continue
        if check(t[i], t[j]):
            print(-1)
            exit()
for i in range(n):
    for j in range(m):
        if check(s[i], t[j]):
            print(-1)
            exit()
for i in range(n):
    for j in range(m):
        if check(t[j], s[i]):
            print(-1)
            exit()
for i in range(n):
    for j in range(m):
        if len(s[i]) + len(t[j]) > 16:
            continue
        for k in range(len(s[i])):
            if s[i][k:] + t[j] == t[j] + s[i][:k]:
                print(s[i][k:] + '_'*(16-len(s[i])-len(t[j])) + t[j])
                exit()
            if t[j][k:] + s[i] == s[i] + t[j][:k]:
                print(t[j][k:] + '_'*(16-len(s[i])-len(t[j])) + s[i])
                exit()
print(-1)

if __name__ == '__main__':
    check()