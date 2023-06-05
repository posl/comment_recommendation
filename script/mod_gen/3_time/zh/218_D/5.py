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
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            if dx == 0 or dy == 0:
                continue
            if x[i] - dy in x and y[i] + dx in y:
                if x[j] - dy in x and y[j] + dx in y:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()