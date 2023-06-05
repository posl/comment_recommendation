def countArithmeticSums(N):
    # 1. 确定公差
    # 2. 确定首项
    # 3. 确定项数
    # 4. 确定和
    # 5. 判断和是否等于N
    # 6. 计数
    # 7. 重复1-6
    # 8. 返回计数
    count = 0
    for d in range(1, N+1):
        for a in range(1, N+1):
            n = 0
            while True:
                n += 1
                sum = n * (2 * a + (n - 1) * d) / 2
                if sum > N:
                    break
                if sum == N:
                    count += 1
    return count
N = int(input())
print(countArithmeticSums(N))
