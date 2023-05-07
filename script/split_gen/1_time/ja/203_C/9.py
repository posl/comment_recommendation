def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    money = K
    i = 0
    while i < N:
        if AB[i][0] <= money:
            money += AB[i][1]
        else:
            break
        i += 1
    print(money)
