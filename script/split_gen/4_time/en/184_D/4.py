def solve():
    A,B,C = map(int, input().split())
    ans = 0
    while A+B+C > 2:
        ans += 1
        if A > 0:
            A -= 1
            B += 1
        elif B > 0:
            B -= 1
            C += 1
        else:
            C -= 1
            A += 1
    print(ans + A/3 + B/3 + C/3)
