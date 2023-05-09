def main():
    # input
    N, K = map(int, input().split())
    Ps = list(map(int, input().split()))
    # compute
    Ps.sort()
    ans = sum(Ps[:K])
    # output
    print(ans)
