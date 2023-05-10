def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [tuple(map(int, input().split())) for _ in range(N)]
    #print(N, K, A, XY)
    print(solve(N, K, A, XY))
