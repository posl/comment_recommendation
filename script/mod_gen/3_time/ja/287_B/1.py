def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    ans = 0
    for s in S:
        ans += sum(s[-3:] == t for t in T)
    print(ans)

if __name__ == '__main__':
    main()