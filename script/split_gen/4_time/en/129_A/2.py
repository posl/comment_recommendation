def main():
    # input
    P, Q, R = map(int, input().split())
    # compute
    # output
    print(min(P+Q, Q+R, R+P))
