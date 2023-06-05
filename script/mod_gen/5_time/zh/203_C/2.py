def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    money = K
    for i in range(N):
        if money < AB[i][0]:
            break
        money += AB[i][1]
    print(money)

if __name__ == '__main__':
    main()