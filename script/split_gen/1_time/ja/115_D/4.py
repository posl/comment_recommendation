def main():
    N, X = map(int, input().split())
    p = 1
    for i in range(N):
        p = p * 2 + 3
    print(solve(N, X, p))
