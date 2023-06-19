def solve():
    n = int(input())
    x = []
    y = []
    h = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        x.append(tmp[0])
        y.append(tmp[1])
        h.append(tmp[2])
    for i in range(101):
        for j in range(101):
            H = 0
            for k in range(n):
                if h[k] != 0:
                    H = h[k] + abs(x[k]-i) + abs(y[k]-j)
                    break
            flag = True
            for k in range(n):
                if max(H - abs(x[k]-i) - abs(y[k]-j), 0) != h[k]:
                    flag = False
                    break
            if flag:
                print(i, j, H)
                return

if __name__ == '__main__':
    solve()