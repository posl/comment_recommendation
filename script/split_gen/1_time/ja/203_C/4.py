def main():
    N, K = map(int, input().split())
    friends = []
    for i in range(N):
        friends.append(list(map(int, input().split())))
    friends.sort()
    for i in range(N):
        if K < friends[i][0]:
            break
        K += friends[i][1]
    print(K)
