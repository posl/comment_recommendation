def solve():
    #import sys
    #input = sys.stdin.readline
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = [0] * (M + 1)
    for i in range(N):
        C[A[i]] += 1
    ans = 0
    for i in range(M):
        if C[i] == 0 and C[(i + 1) % M] == 0:
            continue
        ans += C[i] * i
        C[(i + 1) % M] += C[i]
    print(ans)

if __name__ == '__main__':
    solve()