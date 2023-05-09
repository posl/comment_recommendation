def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > i+1:
            continue
        for j in range(i+1, N):
            if A[j] < j+1:
                continue
            if A[i] == i+1 and A[j] == j+1:
                ans += 1
    print(ans)
    return 0
