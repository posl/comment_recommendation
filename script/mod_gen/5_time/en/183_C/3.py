def main():
    N, K = map(int, input().split())
    T = []
    for _ in range(N):
        T.append(list(map(int, input().split())))
    from itertools import permutations
    ans = 0
    for p in permutations(range(1, N)):
        time = 0
        cur = 0
        for i in p:
            time += T[cur][i]
            cur = i
        time += T[cur][0]
        if time == K:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()