def solve():
    N = int(input())
    ans = ""
    while N > 0:
        if N % 2 == 0:
            N = N // 2
            ans = "B" + ans
        else:
            N -= 1
            ans = "A" + ans
    print(ans)
    return 0
