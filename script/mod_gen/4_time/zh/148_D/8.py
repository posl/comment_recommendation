def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] == i + 1:
            ans += 1
    print(-1 if ans == N else N - ans)
main()
