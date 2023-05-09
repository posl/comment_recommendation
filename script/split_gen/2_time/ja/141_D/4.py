def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i]
        ans = ans // 2
    print(ans)
