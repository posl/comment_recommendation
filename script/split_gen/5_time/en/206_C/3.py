def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    i = 0
    while i < N:
        j = i + 1
        while j < N and A[i] == A[j]:
            j += 1
        ans += (j - i) * (N - j)
        i = j
    print(ans)
solve()
