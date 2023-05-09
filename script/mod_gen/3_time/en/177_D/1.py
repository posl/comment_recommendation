def main():
    N, M = map(int, input().split())
    friends = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        friends[a].append(b)
        friends[b].append(a)
    groups = [0] * N
    group = 1
    for i in range(N):
        if groups[i] == 0:
            groups[i] = group
            q = [i]
            while q:
                p = q.pop()
                for f in friends[p]:
                    if groups[f] == 0:
                        groups[f] = group
                        q.append(f)
            group += 1
    print(group - 1)
main()

if __name__ == '__main__':
    main()