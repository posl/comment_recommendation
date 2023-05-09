def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    CD = [tuple(map(int, input().split())) for _ in range(M)]
    for p in permutations(range(1, N+1)):
        if all(AB[i] in CD[p.index(j)] for i, j in enumerate(p)):
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    main()