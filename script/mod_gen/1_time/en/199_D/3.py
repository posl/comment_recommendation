def main():
    N,M = map(int,input().split())
    if M == 0:
        print(3**N)
        return
    G = [[] for i in range(N)]
    for i in range(M):
        a,b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    ans = 0
    for i in range(3**N):
        flag = True
        for j in range(N):
            for k in G[j]:
                if j > k:
                    continue
                if (i//(3**j))%3 == (i//(3**k))%3:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()