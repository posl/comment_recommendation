def solve(x, y):
    if x + y == 0:
        return 1
    elif x + y == 1:
        return 0
    else:
        # 骑士可以从(i,j)到达(i+1,j+2)或(i+2,j+1)。
        # 从(i+1,j+2)到达(X,Y)的方法数为solve(X-i-1,Y-j-2)。
        # 从(i+2,j+1)到达(X,Y)的方法数为solve(X-i-2,Y-j-1)。
        # 因此，从(i,j)到达(X,Y)的方法数为solve(X-i-1,Y-j-2)+solve(X-i-2,Y-j-1)。
        # 为了避免重复计算，我们使用记忆化递归。
        if (x, y) in memo:
            return memo[(x, y)]
        else:
            memo[(x, y)] = (solve(x - 1, y - 2) + solve(x - 2, y - 1)) % 1000000007
            return memo[(x, y)]
memo = {}
x, y = map(int, input().split())
print(solve(x, y))
