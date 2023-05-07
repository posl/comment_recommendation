def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    mod = [0] * M
    mod[0] = 1
    total = 0
    for i in range(N):
        total = (total + A[i]) % M
        mod[total] += 1
    ans = 0
    for i in range(M):
        ans += mod[i] * (mod[i] - 1) // 2
    print(ans)
