def main():
    # input
    P, Q, R = map(int, input().split())
    # compute
    ans = min(P+Q, Q+R, R+P)
    # output
    print(ans)
