def solve():
    K = int(input())
    ans = 0
    i = 0
    while True:
        if K % 2 == 1:
            ans += 2 * (10 ** i)
            K -= 1
        else:
            ans += 0 * (10 ** i)
        if K == 0:
            break
        K //= 2
        i += 1
    print(ans)
    return 0
