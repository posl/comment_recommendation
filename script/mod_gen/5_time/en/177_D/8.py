def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[0])
    group = [1] * N
    for i in range(M):
        if group[AB[i][0] - 1] == 1:
            group[AB[i][0] - 1] = group[AB[i][1] - 1]
        elif group[AB[i][1] - 1] == 1:
            group[AB[i][1] - 1] = group[AB[i][0] - 1]
        else:
            group[AB[i][1] - 1] = group[AB[i][0] - 1]
    print(len(set(group)))

if __name__ == '__main__':
    main()