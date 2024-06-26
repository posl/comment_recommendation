def main():
    N, K = map(int, input().split())
    friends = []
    for i in range(N):
        A, B = map(int, input().split())
        friends.append((A, B))
    friends.sort()
    money = K
    for i in range(N):
        if money >= friends[i][0]:
            money += friends[i][1]
    print(money)

if __name__ == '__main__':
    main()