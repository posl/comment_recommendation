def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    for c in product("_", repeat=N-1):
        X = "".join(s1 + s2 for s1, s2 in zip(S, c + ("",)))
        if all(X != t for t in T) and 3 <= len(X) <= 16:
            print(X)
            return
    print(-1)

if __name__ == '__main__':
    main()