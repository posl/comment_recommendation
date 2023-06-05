def change_handle(n, s, t):
    if n == 1:
        print('Yes')
        return
    for i in range(n):
        if s[i] == t[i]:
            print('No')
            return
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == t[j] and s[j] == t[i]:
                print('Yes')
                return
    print('No')
    return
n = int(input())
s = []
t = []
for i in range(n):
    tmp = input().split()
    s.append(tmp[0])
    t.append(tmp[1])
change_handle(n, s, t)
