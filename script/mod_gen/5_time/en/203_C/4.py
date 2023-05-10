def main():
    N, K = map(int, input().split())
    friends = []
    for _ in range(N):
        friends.append(list(map(int, input().split())))
    friends.sort(key=lambda x: x[0])
    i = 0
    while K > 0:
        K -= 1
        K += friends[i][1]
        i += 1
    print(friends[i-1][0])

if __name__ == '__main__':
    main()