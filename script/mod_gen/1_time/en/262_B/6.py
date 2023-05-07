def main():
    N, M = map(int, raw_input().split())
    edges = []
    for i in xrange(M):
        edges.append(map(int, raw_input().split()))
    print solve(N, M, edges)

if __name__ == '__main__':
    main()