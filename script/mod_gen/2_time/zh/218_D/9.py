def main():
    N = int(input())
    x = []
    y = []
    for _ in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    d = {}
    for i in range(N):
        d[(x[i], y[i])] = 1
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if x[i] == x[j] or y[i] == y[j]:
                continue
            if (x[i], y[j]) in d and (x[j], y[i]) in d:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()