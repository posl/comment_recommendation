def main():
    N, M = map(int, input().split())
    bridges = [tuple(map(int, input().split())) for _ in range(M)]
    bridges.sort(key=lambda x: x[1])
    count = 0
    last = 0
    for a, b in bridges:
        if last < a:
            last = b - 1
            count += 1
    print(count)

if __name__ == '__main__':
    main()