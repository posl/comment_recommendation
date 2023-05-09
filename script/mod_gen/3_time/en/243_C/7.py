def solve():
    n = int(input())
    x = []
    y = []
    s = []
    for i in range(n):
        x_, y_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
        s.append(input())
    for i in range(n):
        for j in range(i + 1, n):
            if (x[i] - x[j]) * (y[i] - y[j]) > 0:
                if s[i] == s[j]:
                    print("No")
                    return
            else:
                if s[i] != s[j]:
                    print("No")
                    return
    print("Yes")

if __name__ == '__main__':
    solve()