def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i]
        if ans % 2 == 1:
            continue
        if M > 0:
            ans //= 2
            M -= 1
    print(ans)
