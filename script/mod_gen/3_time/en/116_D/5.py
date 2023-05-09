def main():
    N, K = map(int, input().split())
    Sushi = [tuple(map(int, input().split())) for _ in range(N)]
    Sushi.sort(key=lambda x: x[1], reverse=True)
    T = set([s[0] for s in Sushi[:K]])
    S = sum([s[1] for s in Sushi[:K]])
    ans = S + len(T) ** 2
    for i in range(K, N):
        if len(T) == K:
            break
        if Sushi[i][0] in T:
            continue
        T.add(Sushi[i][0])
        S -= Sushi[i-K][1]
        S += Sushi[i][1]
        ans = max(ans, S + len(T) ** 2)
    print(ans)

if __name__ == '__main__':
    main()