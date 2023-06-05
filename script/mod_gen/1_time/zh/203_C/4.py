def main():
    n, k = map(int, input().split())
    friends = []
    for i in range(n):
        a, b = map(int, input().split())
        friends.append((a, b))
    friends.sort()
    friends.append((10**100, 0))
    money = k
    pos = 0
    for i in range(n):
        money += friends[i][1]
        if money >= friends[i+1][0]:
            money -= friends[i+1][0]
            pos = friends[i+1][0]
        else:
            pos += money
            break
    print(pos)

if __name__ == '__main__':
    main()