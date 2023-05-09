def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    for i in range(N):
        A[i+1] += A[i]
    mod = {}
    for i in range(N+1):
        if A[i] % M not in mod:
            mod[A[i] % M] = 0
        mod[A[i] % M] += 1
    ans = 0
    for i in mod:
        ans += mod[i] * (mod[i] - 1) // 2
    print(ans)
