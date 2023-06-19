def solve(N, A):
    MOD = 998244353
    ans = [0] * 10
    for i in range(10):
        for j in range(10):
            cnt = 0
            for k in range(N):
                if k % 2 == 0:
                    if A[k] == i:
                        cnt += 1
                else:
                    if A[k] == j:
                        cnt += 1
            ans[(i * j) % 10] += pow(2, cnt - 1, MOD)
    return [a % MOD for a in ans]
N = int(input())
A = list(map(int, input().split()))
print('
'.join(map(str, solve(N, A))))
