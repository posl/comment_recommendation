def main():
    # input
    N = int(input())
    # compute
    ans = N % 1000
    if ans != 0:
        ans = 1000 - ans
    # output
    print(ans)
