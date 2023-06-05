def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i, N):
            if (A[i] + A[j]) % 2 == 0:
                ans += 1
    print(ans)
