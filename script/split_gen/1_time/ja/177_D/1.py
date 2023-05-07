def main():
    n, m = map(int, input().split())
    friends = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        friends[a-1].append(b-1)
        friends[b-1].append(a-1)
    groups = [set() for _ in range(n)]
    for i in range(n):
        if groups[i]:
            continue
        groups[i].add(i)
        for j in friends[i]:
            if groups[j]:
                continue
            groups[j] = groups[i]
    print(len(set(map(frozenset, groups))))
