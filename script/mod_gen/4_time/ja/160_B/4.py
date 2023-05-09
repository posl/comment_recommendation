def solve():
    X = int(input())
    y = 0
    y += (X // 500) * 1000
    X = X % 500
    y += (X // 5) * 5
    print(y)

if __name__ == '__main__':
    solve()