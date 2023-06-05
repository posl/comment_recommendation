def main():
    N,K = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(N)]
    ab.sort()
    money = K
    village = 0
    for i in range(N):
        if money >= ab[i][0] - village:
            money += ab[i][1]
            village = ab[i][0]
        else:
            break
    village += money
    print(village)
main()
