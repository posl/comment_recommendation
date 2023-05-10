def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    ans = 0
    count = 0
    pre = -1
    for i in range(N + 1):
        if pre == A[i]:
            count += 1
        else:
            ans += count * (count - 1) // 2
            count = 1
            pre = A[i]
    for i in range(N):
        print(ans - (A.index(A[i]) - i) + (N - A.index(A[i]) - 1))
solve()
