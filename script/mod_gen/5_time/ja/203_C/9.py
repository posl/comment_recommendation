def main():
    n,k = map(int, input().split())
    friends = []
    for i in range(n):
        a,b = map(int, input().split())
        friends.append((a,b))
    friends.sort(key=lambda x:x[0])
    #print(friends)
    cnt = 0
    for friend in friends:
        if friend[0] - cnt <= k:
            k += friend[1]
            cnt = friend[0]
        else:
            break
    print(k+cnt)

if __name__ == '__main__':
    main()