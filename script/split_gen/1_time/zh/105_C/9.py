def solve():
    n = int(input())
    if n == 0:
        print(0)
        return
    ans = ''
    while n != 0:
        if n % 2 == 0:
            ans = '0' + ans
            n = n // -2
        else:
            ans = '1' + ans
            n = (n - 1) // -2
    print(ans)
