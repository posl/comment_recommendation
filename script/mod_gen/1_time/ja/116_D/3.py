def main():
    N, K = map(int, input().split())
    sushi = [list(map(int, input().split())) for _ in range(N)]
    sushi.sort(key=lambda x: x[1], reverse=True)
    types = set()
    types.add(sushi[0][0])
    s = sushi[0][1]
    l = 0
    r = 0
    ans = s + len(types) ** 2
    while r < N - 1:
        r += 1
        types.add(sushi[r][0])
        s += sushi[r][1]
        while len(types) > K:
            types.remove(sushi[l][0])
            s -= sushi[l][1]
            l += 1
        ans = max(ans, s + len(types) ** 2)
    print(ans)

if __name__ == '__main__':
    main()