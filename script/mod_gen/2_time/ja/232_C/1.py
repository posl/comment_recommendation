def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(M)]
    for p in permutations(range(1, N + 1)):
        ok = True
        for a, b in AB:
            if (p[a - 1], p[b - 1]) not in CD:
                ok = False
                break
        if ok:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()