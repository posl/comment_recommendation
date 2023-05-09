def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(N)]
    AB.sort(key=lambda x: x[0] + x[1])
    ans = 0
    for i in range(N):
        if X > 1:
            ans += AB[i][0]
            X -= 1
        else:
            ans += AB[i][0] + AB[i][1]
            break
    if X > 1:
        ans += (X - 1) * AB[N - 1][1]
    print(ans)
main()

if __name__ == '__main__':
    main()