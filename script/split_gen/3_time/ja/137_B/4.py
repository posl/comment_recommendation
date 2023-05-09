def main():
    # input
    K, X = map(int, input().split())
    # compute
    # output
    print(*range(X-K+1, X+K))
