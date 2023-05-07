def main():
    import sys
    import itertools
    import math
    N = int(input())
    x = [0] * N
    y = [0] * N
    for i in range(N):
        x[i], y[i] = map(int, input().split())
    ans = 0
    for p in itertools.permutations(range(N)):
        for i in range(N-1):
            ans += math.sqrt((x[p[i]]-x[p[i+1]])**2 + (y[p[i]]-y[p[i+1]])**2)
    ans /= math.factorial(N)
    print(ans)

if __name__ == '__main__':
    main()