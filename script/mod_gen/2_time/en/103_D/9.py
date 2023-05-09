def main():
    N, M = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(M)]
    bridges.sort(key=lambda x: x[1])
    cnt = 0
    last = 0
    for a, b in bridges:
        if last < a:
            cnt += 1
            last = b - 1
    print(M - cnt)

if __name__ == '__main__':
    main()