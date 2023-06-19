def problem179_c():
    N = int(input())
    ans = 0
    for i in range(1, int(N**0.5)+1):
        if N%i == 0:
            m = N//i - 1
            if m > i:
                ans += m
    print(ans)
