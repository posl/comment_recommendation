def main():
    N, M = map(int, input().split())
    bridges = []
    for _ in range(M):
        a, b = map(int, input().split())
        bridges.append([a, b])
    bridges.sort(key=lambda x: x[1])
    ans = 0
    last = 0
    for bridge in bridges:
        if last < bridge[0]:
            last = bridge[1] - 1
            ans += 1
    print(M - ans)

if __name__ == '__main__':
    main()