def main():
    N, M = map(int, input().split())
    edges = []
    for i in range(M):
        edges.append(list(map(int, input().split())))
    edges.sort()
    count = 0
    for i in range(M):
        for j in range(i+1, M):
            if edges[i][1] == edges[j][0]:
                for k in range(j+1, M):
                    if edges[j][1] == edges[k][0] and edges[k][1] == edges[i][0]:
                        count += 1
    print(count)

if __name__ == '__main__':
    main()