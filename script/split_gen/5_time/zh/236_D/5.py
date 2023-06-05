def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    # print(a)
    ans = 0
    for i in range(1, 2**n):
        for j in range(i+1, 2**n):
            if i & j == 0:
                continue
            x = 0
            for k in range(n):
                if (i >> k) & 1 == 1:
                    for l in range(k+1, n):
                        if (i >> l) & 1 == 1:
                            x += a[k][l]
                if (j >> k) & 1 == 1:
                    for l in range(k+1, n):
                        if (j >> l) & 1 == 1:
                            x += a[k][l]
            ans = max(ans, x)
    print(ans)
