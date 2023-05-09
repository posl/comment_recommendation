def main():
    n,m = map(int,input().split())
    friends = [[] for _ in range(n)]
    for i in range(m):
        a,b = map(int,input().split())
        friends[a-1].append(b-1)
        friends[b-1].append(a-1)
    #print(friends)
    group = [-1]*n
    num_group = 0
    for i in range(n):
        if group[i] == -1:
            group[i] = num_group
            num_group += 1
        for j in friends[i]:
            if group[j] == -1:
                group[j] = group[i]
    print(num_group)

if __name__ == '__main__':
    main()