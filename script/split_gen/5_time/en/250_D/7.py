def solve():
    N = int(input())
    ans = 0
    for i in range(1, int(N**(1/3)) + 1):
        if N % i == 0:
            if i**3 < N:
                ans += 1
            if i**3 != N:
                ans += 1
    print(ans)
