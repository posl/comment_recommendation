def main():
    N, K = map(int, input().split())
    sushi = []
    for i in range(N):
        sushi.append(tuple(map(int, input().split())))
    sushi.sort(key=lambda x: x[1], reverse=True)
    #print(sushi)
    kind = {}
    for i in range(K):
        if sushi[i][0] in kind:
            kind[sushi[i][0]] += 1
        else:
            kind[sushi[i][0]] = 1
    #print(kind)
    variety = len(kind.keys())
    #print(variety)
    base = sum([x[1] for x in sushi[:K]])
    #print(base)
    ans = base + variety**2
    #print(ans)
    for i in range(K, N):
        if sushi[i][0] in kind:
            continue
        else:
            if variety == 1:
                continue
            else:
                base = base - sushi[i-K][1] + sushi[i][1]
                variety += 1
                ans = max(ans, base + variety**2)
    print(ans)

if __name__ == '__main__':
    main()