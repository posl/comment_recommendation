def main():
    # input
    N = int(input())
    # compute
    if N % 111 == 0:
        ans = N
    else:
        ans = (N // 111 + 1) * 111
    # output
    print(ans)
