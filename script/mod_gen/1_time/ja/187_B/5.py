def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if (-1 <= (y[i] - y[j]) / (x[i] - x[j]) <= 1):
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()