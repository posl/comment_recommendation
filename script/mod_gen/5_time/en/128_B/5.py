def solve():
    N = int(input())
    S = []
    P = []
    for _ in range(N):
        s, p = input().split()
        S.append(s)
        P.append(int(p))
    for i in range(N):
        print(P.index(sorted(P, reverse=True)[i]) + 1)

if __name__ == '__main__':
    solve()