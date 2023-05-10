def main():
    n, d = map(int, input().split())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    ans = 0
    for i in range(n):
        if x[i] ** 2 + y[i] ** 2 <= d ** 2:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()