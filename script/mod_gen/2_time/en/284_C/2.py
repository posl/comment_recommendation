def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    edges = []
    for _ in range(M):
        edges.append(list(map(int, input().split())))
    edges = sorted(edges, key=lambda x: x[0])
    group = [0] * N
    group[edges[0][0] - 1] = 1
    for i in range(1, N):
        if edges[i][0] == edges[i - 1][0]:
            group[edges[i][0] - 1] = group[edges[i - 1][0] - 1]
        else:
            group[edges[i][0] - 1] = group[edges[i - 1][0] - 1] + 1
    for i in range(M):
        group[edges[i][1] - 1] = group[edges[i][0] - 1]
    print(max(group))

if __name__ == '__main__':
    main()