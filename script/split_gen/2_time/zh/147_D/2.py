def main():
    n = int(input())
    a = []
    x = []
    y = []
    for i in range(n):
        a.append(int(input()))
        t_x = []
        t_y = []
        for j in range(a[i]):
            tmp = input().split()
            t_x.append(int(tmp[0]))
            t_y.append(int(tmp[1]))
        x.append(t_x)
        y.append(t_y)
    ans = 0
    for i in range(1<<n):
        flag = True
        cnt = 0
        for j in range(n):
            if i>>j & 1:
                cnt += 1
                for k in range(a[j]):
                    if y[j][k] == 1 and not (i>>(x[j][k]-1) & 1):
                        flag = False
                    if y[j][k] == 0 and (i>>(x[j][k]-1) & 1):
                        flag = False
        if flag:
            ans = max(ans, cnt)
    print(ans)
