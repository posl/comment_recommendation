def main():
    # input
    N, K = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(N)]
    # compute
    ab.sort()
    for a, b in ab:
        if a > K:
            break
        K += b
    # output
    print(K)
