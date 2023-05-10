def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    count = 0
    for i in range(N):
        if count + AB[i][0] <= M:
            ans += AB[i][0] * AB[i][1]
            count += AB[i][0]
        else:
            ans += (M - count) * AB[i][1]
            break
    print(ans)

if __name__ == '__main__':
    main()