def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    x.sort()
    y.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    if x[i] == x[j] and y[k] == y[l] and x[k] == x[l] and y[i] == y[j]:
                        ans += 1
    print(ans)

if __name__ == '__main__':
    main()