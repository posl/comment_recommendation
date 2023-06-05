def solve():
    N = int(input())
    res = ""
    while N > 0:
        N -= 1
        res = chr(ord('a') + N % 26) + res
        N //= 26
    print(res)
solve()
