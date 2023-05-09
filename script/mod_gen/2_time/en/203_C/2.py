def main():
    n, k = map(int, input().split())
    friends = []
    for i in range(n):
        a, b = map(int, input().split())
        friends.append((a, b))
    friends.sort(key=lambda x: x[0])
    money = k
    village = 0
    for friend in friends:
        if money >= friend[0] - village:
            money += friend[1] - (friend[0] - village)
            village = friend[0]
        else:
            break
    village += money
    print(village)

if __name__ == '__main__':
    main()