def main():
    n, k = map(int, input().split())
    friends = []
    for _ in range(n):
        friends.append(list(map(int, input().split())))
    friends.sort(key=lambda x: x[0])
    money = k
    village = 0
    for i in range(n):
        if friends[i][0] <= village:
            money += friends[i][1]
        else:
            if friends[i][0] - village > money:
                break
            else:
                money -= friends[i][0] - village
                money += friends[i][1]
                village = friends[i][0]
    print(village + money)
