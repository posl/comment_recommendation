def solve(K):
    # 1. 2~K之间的偶数个数
    # 2. 1~K之间的奇数个数
    # 3. 1.2的组合
    # 4. 3的和
    # 5. 4的平方
    return (K//2) * ((K+1)//2)
print(solve(3))
print(solve(6))
print(solve(11))
print(solve(50))
