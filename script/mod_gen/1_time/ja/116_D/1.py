def main():
    N, K = map(int, input().split())
    sushi = []
    for _ in range(N):
        t, d = map(int, input().split())
        sushi.append((t, d))
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi = sushi[:K]
    ans = 0
    ans += sum([s[1] for s in sushi])
    ans += len(set([s[0] for s in sushi])) ** 2
    types = [s[0] for s in sushi]
    for s in sushi:
        if types.count(s[0]) > 1:
            types.remove(s[0])
            continue
        for s2 in sushi:
            if s[0] == s2[0]:
                continue
            if len(types) == K:
                break
            if types.count(s2[0]) == 0:
                types.append(s2[0])
                ans += s2[1]
                break
    print(ans)

if __name__ == '__main__':
    main()