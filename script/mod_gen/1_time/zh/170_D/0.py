def solve():
    N = int(input())
    A = list(map(int, input().split()))
    maxA = max(A)
    count = [0 for i in range(maxA+1)]
    for a in A:
        count[a] += 1
    ans = 0
    for a in A:
        if count[a] == 1:
            ans += 1
    print(ans)
solve()
