def solve():
    n = int(input())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    s = input()
    # 从左到右，从右到左，从上到下，从下到上
    # 4种情况，有一种情况满足即可
    for i in range(4):
        # 从左到右
        if i == 0:
            left = min(x)
            right = max(x)
            for i in range(n):
                if s[i] == 'R':
                    x[i] += 1
            if min(x) <= left and max(x) >= right:
                print('Yes')
                return
        # 从右到左
        elif i == 1:
            left = min(x)
            right = max(x)
            for i in range(n):
                if s[i] == 'L':
                    x[i] -= 1
            if min(x) <= left and max(x) >= right:
                print('Yes')
                return
        # 从上到下
        elif i == 2:
            up = max(y)
            down = min(y)
            for i in range(n):
                if s[i] == 'U':
                    y[i] += 1
            if min(y) <= down and max(y) >= up:
                print('Yes')
                return
        # 从下到上
        else:
            up = max(y)
            down = min(y)
            for i in range(n):
                if s[i] == 'D':
                    y[i] -= 1
            if min(y) <= down and max(y) >= up:
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    solve()