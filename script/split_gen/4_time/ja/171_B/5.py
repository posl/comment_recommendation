def main():
    # input
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    # compute
    p.sort()
    ans = 0
    for i in range(K):
        ans += p[i]
    # output
    print(ans)
