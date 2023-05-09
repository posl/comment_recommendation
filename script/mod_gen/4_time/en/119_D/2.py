def main():
    A, B, Q = map(int, input().split())
    s = [-10**20] + [int(input()) for _ in range(A)] + [10**20]
    t = [-10**20] + [int(input()) for _ in range(B)] + [10**20]
    x = [int(input()) for _ in range(Q)]
    for xi in x:
        ans = 10**20
        for si in s:
            for ti in t:
                if si <= xi and xi <= ti:
                    ans = min(ans, abs(xi - si) + abs(ti - si))
                elif si <= xi and xi <= ti:
                    ans = min(ans, abs(xi - ti) + abs(si - ti))
                elif si <= xi and xi <= ti:
                    ans = min(ans, abs(xi - si) + abs(ti - si))
                else:
                    ans = min(ans, abs(xi - si) + abs(ti - si))
        print(ans)

if __name__ == '__main__':
    main()