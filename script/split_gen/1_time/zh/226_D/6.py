def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            a = x[i] - x[j]
            b = y[i] - y[j]
            cnt = 0
            for k in range(n):
                for l in range(k+1, n):
                    if x[k] - x[l] == a and y[k] - y[l] == b:
                        cnt += 1
            ans = max(ans, n - cnt)
    print(ans)
main()
