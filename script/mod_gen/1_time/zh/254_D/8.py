def solve(n):
    from math import sqrt
    # 1. 计算1~n的平方数
    squares = [x*x for x in range(1, int(sqrt(n))+1)]
    # 2. 计算1~n的平方数的个数
    cnt = 0
    for i in range(1, int(sqrt(n))+1):
        cnt += n//i
    # 3. 从1~n中减去不满足条件的数
    for square in squares:
        cnt -= n//square
    return cnt
n = int(input())
print(solve(n))
