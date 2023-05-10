def main():
    N,K = map(int, input().split())
    friends = []
    for i in range(N):
        A,B = map(int, input().split())
        friends.append([A,B])
    friends.sort()
    i = 0
    while K > 0 and i < N:
        if friends[i][0] <= K:
            K += friends[i][1]
            i += 1
        else:
            break
    print(K)
main()

if __name__ == '__main__':
    main()