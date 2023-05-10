def get_inputs():
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]
    return N, xy
