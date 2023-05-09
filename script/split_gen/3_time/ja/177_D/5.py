def main():
    N, M = map(int, input().split())
    friends = [list(map(int, input().split())) for _ in range(M)]
    friend_list = [[] for _ in range(N)]
    for i in range(M):
        friend_list[friends[i][0]-1].append(friends[i][1]-1)
        friend_list[friends[i][1]-1].append(friends[i][0]-1)
    #print(friend_list)
    group = 0
    for i in range(N):
        if friend_list[i] == []:
            group += 1
            continue
        if i in friend_list[i]:
            group += 1
            continue
        for j in friend_list[i]:
            if j in friend_list[j]:
                group += 1
                break
    print(group)
