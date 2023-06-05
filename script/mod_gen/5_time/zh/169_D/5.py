def solve():
    N = int(input())
    ans = 0
    for i in range(2, int(N**0.5)+1):
        if N%i==0:
            ans += 1
            while N%i==0:
                N //= i
    if N > 1:
        ans += 1
    print(ans)
solve()
