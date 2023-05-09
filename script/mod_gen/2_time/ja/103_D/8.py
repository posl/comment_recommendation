def main():
    N, M = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(M)]
    bridges.sort()
    print(bridges)
    print(M - N + 1)

if __name__ == '__main__':
    main()