def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = list(map(lambda x: x//2, A))
    lcm = A[0]
    for a in A[1:]:
        lcm = lcm * a // gcd(lcm, a)
    if lcm > M:
        return 0
    return (M//lcm+1)//2
