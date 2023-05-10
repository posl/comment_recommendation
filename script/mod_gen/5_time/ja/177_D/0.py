def main():
    N, M = map(int, input().split())
    friends = []
    for i in range(M):
        friends.append(list(map(int, input().split())))
    print(friends)
    #friends = [[1, 2], [3, 4], [5, 1]]
    #friends = [[1, 2], [2, 1], [1, 2], [2, 1], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    #friends = [[3, 1], [4, 1], [5, 9], [2, 6]]
    #N = 10
    #M = 4
    friend_group = [[0] * N for i in range(N)]
    for i in range(M):
        friend_group[friends[i][0] - 1][friends[i][1] - 1] = 1
        friend_group[friends[i][1] - 1][friends[i][0] - 1] = 1
    print(friend_group)
    for i in range(N):
        for j in range(N):
            if friend_group[i][j] == 1:
                for k in range(N):
                    if friend_group[j][k] == 1:
                        friend_group[i][k] = 1
                        friend_group[k][i] = 1
    print(friend_group)
    result = 0
    for i in range(N):
        if sum(friend_group[i]) == 0:
            result += 1
    print(result)

if __name__ == '__main__':
    main()