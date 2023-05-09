def main():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        u, v = map(int, input().split())
        edges.append([u, v])
    print(N, M, edges)

if __name__ == '__main__':
    main()