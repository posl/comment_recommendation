def main():
    n = int(input())
    a = []
    xy = []
    for i in range(n):
        a.append(int(input()))
        xy.append([])
        for j in range(a[i]):
            xy[i].append(list(map(int, input().split())))
    ans = 0
    for i in range(1 << n):
        flag = True
        for j in range(n):
            if (i >> j) & 1:
                for k in range(a[j]):
                    if ((i >> (xy[j][k][0] - 1)) & 1) ^ xy[j][k][1]:
                        flag = False
                        break
                if not flag:
                    break
        if flag:
            ans = max(ans, bin(i).count("1"))
    print(ans)
