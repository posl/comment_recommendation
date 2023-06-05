def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    money = K
    for a, b in AB:
        if a <= money:
            money += b
        else:
            break
    print(money)
