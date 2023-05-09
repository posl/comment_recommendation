def main():
    # input
    x, a, d, n = map(int, input().split())
    # compute
    ans = 0
    if d == 0:
        if x == a:
            ans = 0
        else:
            ans = 1
    else:
        if (x - a) % d == 0:
            ans = (x - a) // d
            if ans < 0:
                ans = -ans
        else:
            ans = 1
    # output
    print(ans)
