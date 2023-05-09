def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        ans += AB[i][0] * AB[i][1]
        if ans > X:
            print(ans)
            exit()
    print(ans)

if __name__ == '__main__':
    main()