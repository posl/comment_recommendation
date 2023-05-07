def check_honest(n, a, x, y):
    for i in range(n):
        if a[i] == 0:
            continue
        for j in range(a[i]):
            if y[i][j] == 1:
                if a[x[i][j]-1] == 0:
                    continue
                else:
                    if y[x[i][j]-1][a[x[i][j]-1]-1] == 1:
                        continue
                    else:
                        return False
            else:
                if a[x[i][j]-1] == 0:
                    continue
                else:
                    if y[x[i][j]-1][a[x[i][j]-1]-1] == 0:
                        continue
                    else:
                        return False
    return True
n = int(input())
a = []
x = []
y = []
for i in range(n):
    a.append(int(input()))
    x.append([])
    y.append([])
    for j in range(a[i]):
        x[i].append(0)
        y[i].append(0)
        x[i][j], y[i][j] = map(int, input().split())
ans = 0
for i in range(2**n):
    tmp = []
    for j in range(n):
        tmp.append((i>>j)&1)
    tmp.reverse()
    tmp_ans = 0
    for j in range(n):
        if tmp[j] == 1:
            tmp_ans += 1
    if tmp_ans <= ans:
        continue
    if check_honest(n, tmp, x, y):
        ans = tmp_ans
print(ans)
