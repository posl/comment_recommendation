def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    print(solve(N, W, A))
