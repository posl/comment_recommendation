def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    money = K
    village = 0
    for i in range(N):
        if money >= AB[i][0] - village:
            money += AB[i][1]
            village = AB[i][0]
        else:
            break
    print(village + money)
