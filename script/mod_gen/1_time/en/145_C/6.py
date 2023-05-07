def main():
    import sys
    from itertools import permutations
    from math import sqrt
    N = int(sys.stdin.readline())
    towns = []
    for i in range(N):
        x,y = map(int,sys.stdin.readline().split())
        towns.append((x,y))
    ans = 0
    for p in permutations(towns):
        for i in range(N-1):
            ans += sqrt((p[i][0]-p[i+1][0])**2+(p[i][1]-p[i+1][1])**2)
    print(ans/N)

if __name__ == '__main__':
    main()