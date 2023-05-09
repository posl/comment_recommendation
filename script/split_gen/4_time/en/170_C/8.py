def main():
    # input
    X, N = map(int, input().split())
    p = list(map(int, input().split()))
    # compute
    # output
    print(solve(X, N, p))
