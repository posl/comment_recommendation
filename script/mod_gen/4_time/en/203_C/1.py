def problems203_c():
    N, K = map(int, input().split())
    friends = []
    for i in range(N):
        A, B = map(int, input().split())
        friends.append([A, B])
    friends = sorted(friends, key=lambda x:x[0])
    for i in range(N):
        if friends[i][0] > K:
            break
        else:
            K += friends[i][1]
    print(K)
problems203_c()

if __name__ == '__main__':
    problems203_c()