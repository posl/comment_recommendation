def main():
    N,K = map(int,input().split())
    S = []
    for i in range(N):
        S.append(input())
    ans = 0
    for i in range(1<<N):
        if bin(i).count("1") == K:
            tmp = set()
            for j in range(N):
                if i & (1<<j):
                    tmp |= set(S[j])
            if len(tmp) == K:
                ans = max(ans,bin(i).count("1"))
    print(ans)

if __name__ == '__main__':
    main()