def main():
    import sys
    from itertools import permutations
    input = sys.stdin.readline
    N = int(input())
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    ans = 0
    for p in permutations(range(N)):
        for i in range(N-1):
            ans += ((X[p[i]]-X[p[i+1]])**2+(Y[p[i]]-Y[p[i+1]])**2)**0.5
    print(ans/N)

if __name__ == '__main__':
    main()