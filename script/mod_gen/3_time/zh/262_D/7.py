def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, 2**N):
        sum = 0
        cnt = 0
        for j in range(N):
            if i & (1 << j):
                sum += A[j]
                cnt += 1
        if sum % cnt == 0:
            ans += 1
    print(ans)
solve()
