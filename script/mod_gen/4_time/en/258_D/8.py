def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(N)]
    AB.sort(key=lambda x: x[0] + x[1])
    ans = 0
    for i in range(N):
        ans += AB[i][0] + AB[i][1]
        if ans > X:
            print(i + 1)
            exit()
    print(N)

if __name__ == '__main__':
    main()