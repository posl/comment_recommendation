def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x1, y1 = map(int, input().split())
        x.append(x1)
        y.append(y1)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if x[i] == x[j] or y[i] == y[j]:
                ans = max(ans, abs(x[i]-x[j])+abs(y[i]-y[j]))
    print(ans)

if __name__ == '__main__':
    main()