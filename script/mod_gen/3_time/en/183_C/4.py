def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for p in permutations(range(1, N)):
        t = 0
        for i in range(N-1):
            t += T[p[i-1]][p[i]]
        t += T[0][p[0]]
        t += T[p[N-2]][0]
        if t == K:
            count += 1
    print(count)

if __name__ == '__main__':
    main()