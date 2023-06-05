def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans1 = 0
    ans2 = 0
    for i in range(N):
        if A[i] == B[i]:
            ans1 += 1
    for i in range(N):
        for j in range(N):
            if i != j:
                if A[i] == B[j]:
                    ans2 += 1
    print(ans1)
    print(ans2//2)
solve()
