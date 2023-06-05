def solve(n, a):
    ans = 0
    while True:
        flag = False
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] //= 2
                flag = True
                ans += 1
                break
        if not flag:
            break
    return ans
