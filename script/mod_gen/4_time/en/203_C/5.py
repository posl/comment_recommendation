def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    money = K
    village = 0
    for i in range(N):
        if village < AB[i][0] and money >= AB[i][0] - village:
            money -= AB[i][0] - village
            money += AB[i][1]
            village = AB[i][0]
    village += money
    print(village)

if __name__ == '__main__':
    main()