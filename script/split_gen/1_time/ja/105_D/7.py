def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        A[i] %= M
    #print(A)
    mod = [0] * M
    mod[0] = 1
    sum = 0
    for i in range(N):
        sum += A[i]
        sum %= M
        mod[sum] += 1
    #print(mod)
    ans = 0
    for i in range(M):
        ans += mod[i] * (mod[i] - 1) // 2
    print(ans)
