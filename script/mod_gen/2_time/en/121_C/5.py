def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    money = 0
    for i in range(N):
        if M <= AB[i][1]:
            money += AB[i][0] * M
            break
        else:
            money += AB[i][0] * AB[i][1]
            M -= AB[i][1]
    print(money)

if __name__ == '__main__':
    main()