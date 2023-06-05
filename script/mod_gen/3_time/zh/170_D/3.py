def solve(N, A):
    # 1. 从小到大排序
    A.sort()
    # 2. 从小到大累加
    # 3. 按照条件减去
    ans = 0
    for i in range(N):
        ans += i
        if i > 0 and A[i] == A[i - 1]:
            ans -= 1
    return ans

if __name__ == '__main__':
    solve()