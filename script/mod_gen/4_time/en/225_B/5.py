def main():
    N = int(input())
    edges = [set() for i in range(N+1)]
    for i in range(N-1):
        a, b = map(int, input().split())
        edges[a].add(b)
        edges[b].add(a)
    for i in range(1, N+1):
        if len(edges[i]) == N-1:
            print('Yes')
            exit()
    print('No')
main()

if __name__ == '__main__':
    main()