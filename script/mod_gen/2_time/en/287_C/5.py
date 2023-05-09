def main():
    N, M = map(int, input().split())
    if M != N - 1:
        print('No')
        return
    visited = [False] * N
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        if visited[u] or visited[v]:
            print('No')
            return
        visited[u] = True
        visited[v] = True
    print('Yes')

if __name__ == '__main__':
    main()