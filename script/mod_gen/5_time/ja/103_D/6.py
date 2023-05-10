def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    ans = 0
    bridge = 0
    for i in range(M):
        if bridge < AB[i][0]:
            bridge = AB[i][1] - 1
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()