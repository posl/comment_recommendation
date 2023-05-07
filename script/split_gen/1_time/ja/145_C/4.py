def main():
    import sys
    from itertools import permutations
    input = sys.stdin.readline
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    d = 0
    for p in permutations(range(N)):
        for i in range(N-1):
            d += ((XY[p[i]][0]-XY[p[i+1]][0])**2+(XY[p[i]][1]-XY[p[i+1]][1])**2)**0.5
    print(d/N)
