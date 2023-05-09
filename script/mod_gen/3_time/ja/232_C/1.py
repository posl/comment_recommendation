def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(M)]
    P = list(range(1, N + 1))
    for p in permutations(P):
        if all(AB[i][0] == CD[p[AB[i][0] - 1] - 1][0] and AB[i][1] == CD[p[AB[i][1] - 1] - 1][1] for i in range(M)):
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    main()