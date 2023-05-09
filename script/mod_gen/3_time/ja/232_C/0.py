def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(M)]
    p = [i for i in range(1, N + 1)]
    for i in range(M):
        for j in range(M):
            if AB[i] == CD[j]:
                p[AB[i][0] - 1], p[AB[i][1] - 1] = p[AB[i][1] - 1], p[AB[i][0] - 1]
    if p == [i for i in range(1, N + 1)]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()