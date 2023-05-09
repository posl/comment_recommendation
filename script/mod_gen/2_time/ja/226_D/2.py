def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    x.sort()
    y.sort()
    ans = 0
    for i in range(N):
        for j in range(N):
            if i != j:
                ans += abs(x[i] - x[j]) + abs(y[i] - y[j])
    ans //= N
    print(ans)

if __name__ == '__main__':
    main()