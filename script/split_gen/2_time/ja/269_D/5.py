def main():
    N = int(input())
    XY = [list(map(int, input().split())) for i in range(N)]
    print(solve(N, XY))
