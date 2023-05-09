def main():
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]
    import itertools
    dist = 0
    for p in itertools.permutations(range(N)):
        for i in range(N-1):
            dist += ((xy[p[i]][0]-xy[p[i+1]][0])**2+(xy[p[i]][1]-xy[p[i+1]][1])**2)**0.5
    print(dist/itertools.permutations(range(N)))
