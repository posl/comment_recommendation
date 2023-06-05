def main():
    n,m = map(int,input().split())
    friends = {}
    for i in range(m):
        a,b = map(int,input().split())
        if a in friends:
            friends[a].append(b)
        else:
            friends[a] = [b]
        if b in friends:
            friends[b].append(a)
        else:
            friends[b] = [a]
    #print(friends)
    people = set(range(1,n+1))
    #print(people)
    groups = []
    while people:
        group = set()
        queue = [people.pop()]
        while queue:
            p = queue.pop(0)
            group.add(p)
            if p in friends:
                for f in friends[p]:
                    if f in people:
                        queue.append(f)
                        people.remove(f)
        groups.append(group)
    print(len(groups)-1)

if __name__ == '__main__':
    main()