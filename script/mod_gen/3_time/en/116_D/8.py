def main():
    N,K = map(int,input().split())
    sushi = [tuple(map(int,input().split())) for _ in range(N)]
    sushi.sort(key=lambda x:x[1],reverse=True)
    #print(sushi)
    ans = 0
    for i in range(K):
        ans += sushi[i][1]
    #print(ans)
    kinds = set()
    for i in range(K):
        kinds.add(sushi[i][0])
    #print(kinds)
    if len(kinds) == K:
        print(ans + len(kinds)**2)
    else:
        for i in range(K,N):
            if len(kinds) == K:
                break
            if sushi[i][0] not in kinds:
                kinds.add(sushi[i][0])
                ans += sushi[i][1]
        print(ans + len(kinds)**2)

if __name__ == '__main__':
    main()