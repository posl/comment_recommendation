def main():
    N, M = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(M)]
    bridges.sort(key=lambda x: x[1])
    ans = 0
    prev = 0
    for i in range(M):
        if prev < bridges[i][0]:
            ans += 1
            prev = bridges[i][1]
    print(ans)
main()

if __name__ == '__main__':
    main()