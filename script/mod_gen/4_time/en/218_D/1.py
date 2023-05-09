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
            for k in range(j+1, N):
                for l in range(k+1, N):
                    if (x[i] == x[j] and y[i] == y[k] and x[l] == x[k] and y[l] == y[j]) or (x[i] == x[k] and y[i] == y[j] and x[l] == x[j] and y[l] == y[k]):
                        ans += 1
    print(ans)

if __name__ == '__main__':
    main()