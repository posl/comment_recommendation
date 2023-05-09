def main():
    import math
    import itertools
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for p in itertools.permutations(range(N)):
        for i in range(N-1):
            ans += math.sqrt((XY[p[i]][0]-XY[p[i+1]][0])**2 + (XY[p[i]][1]-XY[p[i+1]][1])**2)
    print(ans/math.factorial(N))

if __name__ == '__main__':
    main()