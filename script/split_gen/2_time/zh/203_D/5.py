def main():
    n, k = map(int, input().split())
    friends = []
    for i in range(n):
        friends.append(list(map(int, input().split())))
    friends = sorted(friends, key=lambda x: x[0])
    # print(friends)
    money = k
    village = 0
    for i in range(n):
        if money >= friends[i][0] - village:
            money += friends[i][1]
            village = friends[i][0]
        else:
            break
    print(village + money)
