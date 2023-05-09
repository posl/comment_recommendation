def solve():
    K = int(input())
    ans = 0
    for i in range(1, 64):
        for j in range(1, 64):
            if i+j-1 > 60:
                break
            if K == 0:
                break
            ans += 2**(i+j-1) * 2**i * (K%2)
            K //= 2
    print(ans)
