def main():
    N, M = map(int, input().split())
    bridges = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        bridges[a - 1].add(b - 1)
        bridges[b - 1].add(a - 1)
    print(N - 1 - max(len(bridge) for bridge in bridges))

if __name__ == '__main__':
    main()