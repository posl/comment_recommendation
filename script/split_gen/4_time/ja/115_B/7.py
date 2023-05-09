def main():
    # input
    N = int(input())
    P = [int(input()) for _ in range(N)]
    # compute
    P.sort()
    P[-1] //= 2
    ans = sum(P)
    # output
    print(ans)
