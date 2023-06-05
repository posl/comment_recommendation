def main():
    N, M = map(int, input().split())
    bridges = []
    for i in range(M):
        a, b = map(int, input().split())
        bridges.append((a, b))
    bridges.sort()
    print(bridges)
    print(N, M)

if __name__ == '__main__':
    main()