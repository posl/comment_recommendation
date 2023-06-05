def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        even = 0
        for i in range(N):
            if A[i] % 2 == 1:
                break
            else:
                even += 1
        if even == N:
            ans += 1
            for i in range(N):
                A[i] //= 2
        else:
            break
    print(ans)
