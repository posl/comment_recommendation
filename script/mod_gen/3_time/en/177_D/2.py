def main():
    N, M = map(int, input().split())
    friends = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a-1].add(b-1)
        friends[b-1].add(a-1)
    for i in range(N):
        if friends[i]:
            for j in friends[i]:
                friends[i] |= friends[j]
    print(len({frozenset(f) for f in friends}))

if __name__ == '__main__':
    main()