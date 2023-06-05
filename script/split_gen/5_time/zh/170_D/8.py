def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if i == 0 or A[i] != A[i - 1]:
            ok = True
            for j in range(i + 1, N):
                if A[j] % A[i] == 0:
                    ok = False
                    break
            if ok:
                ans += 1
    print(ans)
