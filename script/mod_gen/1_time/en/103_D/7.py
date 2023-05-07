def main():
    N, M = map(int, input().split())
    bridges = [tuple(map(int, input().split())) for _ in range(M)]
    bridges.sort(key=lambda x: x[1])
    count = 1
    bridge = bridges[0]
    for i in range(1, M):
        if bridge[1] < bridges[i][0]:
            bridge = bridges[i]
            count += 1
    print(M-count)

if __name__ == '__main__':
    main()