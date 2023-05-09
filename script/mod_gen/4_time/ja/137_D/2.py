def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        if M <= AB[i][0]:
            ans += AB[i][1]
            break
        else:
            ans += AB[i][0] * AB[i][1]
            M -= AB[i][0]
    print(ans)

if __name__ == '__main__':
    main()