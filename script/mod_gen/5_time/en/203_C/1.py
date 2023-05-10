def main():
    N, K = map(int, input().split())
    friends = []
    for i in range(N):
        A, B = map(int, input().split())
        friends.append([A, B])
    friends.sort()
    for i in range(N):
        if K < friends[i][0]:
            break
        K += friends[i][1]
    print(K)

if __name__ == '__main__':
    main()