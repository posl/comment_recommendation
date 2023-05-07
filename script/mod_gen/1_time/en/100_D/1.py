def main():
    n, m = map(int, input().split())
    x = [0] * n
    y = [0] * n
    z = [0] * n
    for i in range(n):
        x[i], y[i], z[i] = map(int, input().split())
    ans = 0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                a = [0] * n
                for l in range(n):
                    if i == 0:
                        a[l] += x[l]
                    else:
                        a[l] -= x[l]
                    if j == 0:
                        a[l] += y[l]
                    else:
                        a[l] -= y[l]
                    if k == 0:
                        a[l] += z[l]
                    else:
                        a[l] -= z[l]
                a.sort(reverse=True)
                b = 0
                for l in range(m):
                    b += a[l]
                ans = max(ans, b)
    print(ans)

if __name__ == '__main__':
    main()