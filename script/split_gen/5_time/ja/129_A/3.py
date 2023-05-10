def main():
    # input
    P, Q, R = map(int, input().split())
    # compute
    ans = P + Q + R - max(P, Q, R)
    # output
    print(ans)
