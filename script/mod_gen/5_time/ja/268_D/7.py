def check(s,t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if t[i] != '_' and s[i] != t[i]:
            return False
    return True
n,m = map(int,input().split())
s = [input() for _ in range(n)]
t = [input() for _ in range(m)]
for i in range(1<<n):
    tmp = ''
    for j in range(n):
        if i & (1<<j):
            tmp += s[j] + '_'
        else:
            tmp += '_' + s[j]
    flag = True
    for j in range(m):
        if check(tmp,t[j]):
            flag = False
            break
    if flag:
        print(tmp)
        exit()
print(-1)

if __name__ == '__main__':
    check()