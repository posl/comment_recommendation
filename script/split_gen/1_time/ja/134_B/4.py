def main():
    # input
    N, D = map(int, input().split())
    # compute
    ans = N//(2*D+1)
    if N%(2*D+1) != 0:
        ans += 1
    # output
    print(ans)
