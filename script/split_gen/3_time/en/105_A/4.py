def main():
    # read input
    N, K = map(int, input().split())
    # calculate
    if N % K == 0:
        ans = 0
    else:
        ans = 1
    # print output
    print(ans)
