def main():
    n = int(raw_input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, raw_input().split())
        x.append(a)
        y.append(b)
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j]:
                continue
            if (x[i], y[j]) in zip(x, y) and (x[j], y[i]) in zip(x, y):
                ans += 1
    print ans

if __name__ == '__main__':
    main()