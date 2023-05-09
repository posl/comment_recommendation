def solve(N, K, a):
    a.sort()
    ans = [0] * N
    count = 0
    while K > 0:
        if count == N:
            for i in range(N):
                ans[i] += K // N
            K %= N
        else:
            if K >= N - count:
                K -= N - count
                ans[count] += 1
            else:
                ans[count + K] += 1
                K = 0
        count += 1
    return ans

if __name__ == '__main__':
    solve()