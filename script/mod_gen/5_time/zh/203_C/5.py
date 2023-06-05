def main():
    N,K = map(int,input().split())
    friends = []
    for i in range(N):
        friends.append(list(map(int,input().split())))
    friends.sort()
    # print(friends)
    for i in range(N):
        if friends[i][0] > K:
            break
        K += friends[i][1]
    print(K)

if __name__ == '__main__':
    main()