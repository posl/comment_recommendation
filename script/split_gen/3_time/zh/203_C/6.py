def main():
    n,k = map(int, input().split())
    friends = []
    for i in range(n):
        friends.append(list(map(int, input().split())))
    friends.sort(key=lambda x: x[0])
    money = k
    current = 0
    for i in range(n):
        if money >= friends[i][0] - current:
            money += friends[i][1]
        else:
            print(current + money)
            return
        current = friends[i][0]
    print(current + money)
