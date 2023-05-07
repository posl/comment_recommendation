def main():
    N, M = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(M)]
    ans = 0
    for a in range(1, N):
        for b in range(a+1, N):
            for c in range(b+1, N+1):
                if [a, b] in ab and [b, c] in ab and [c, a] in ab:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()