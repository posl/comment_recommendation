def main():
    from itertools import permutations
    import math
    N = int(input())
    towns = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for p in permutations(range(N)):
        for i in range(N-1):
            ans += math.sqrt((towns[p[i]][0]-towns[p[i+1]][0])**2 + (towns[p[i]][1]-towns[p[i+1]][1])**2)
    print(ans/math.factorial(N))

if __name__ == '__main__':
    main()