def solve(n):
    ans = 0
    for i in range(1, 10**6+1):
        s = i*(i-1)//2
        if s > n:
            break
        if (n-s)%i == 0:
            ans += 1
    return ans*2
