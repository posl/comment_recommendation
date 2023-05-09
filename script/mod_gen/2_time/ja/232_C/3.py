def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    CD = [tuple(map(int, input().split())) for _ in range(M)]
    for p in permutations(range(1, N + 1)):
        if all(AB[i] in CD[p[i - 1] - 1] for i in range(1, N + 1)):
            print('Yes')
            exit()
    print('No')

if __name__ == '__main__':
    main()