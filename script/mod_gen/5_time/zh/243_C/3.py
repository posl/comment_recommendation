def solve():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_, y_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
    s = input()
    for i in range(n):
        if s[i] == 'R':
            x[i] += 1
        elif s[i] == 'L':
            x[i] -= 1
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] and y[i] == y[j]:
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    solve()