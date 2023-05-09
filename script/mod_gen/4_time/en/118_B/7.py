def main():
    N, M = map(int, input().split())
    foods = [set() for _ in range(M)]
    for i in range(N):
        K, *A = map(int, input().split())
        for a in A:
            foods[a-1].add(i)
    ans = 0
    for f in foods:
        if len(f) == N:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()