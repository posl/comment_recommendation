def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i]
    for i in range(N-1):
        ans += min(2*R, 2*L)
    ans += min(2*R, 2*L)
    print(ans)
