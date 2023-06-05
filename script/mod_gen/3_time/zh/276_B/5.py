def main():
    N, M = map(int, input().split())
    edge = [[] for i in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        edge[A-1].append(B)
        edge[B-1].append(A)
    for i in range(N):
        edge[i].sort()
    for i in range(N):
        print(len(edge[i]), end=' ')
        for j in range(len(edge[i])):
            print(edge[i][j], end=' ')
        print()

if __name__ == '__main__':
    main()