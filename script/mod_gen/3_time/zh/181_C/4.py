def solve():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (x[i] - x[j]) * (y[j] - y[k]) == (x[j] - x[k]) * (y[i] - y[j]):
                    print("Yes")
                    return
    print("No")
    return

if __name__ == '__main__':
    solve()