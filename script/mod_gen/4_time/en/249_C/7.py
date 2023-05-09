def main():
    N,K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(2**26):
        cnt = 0
        for s in S:
            if sum(1 for j in s if (i>>ord(j)-97)&1)>0:
                cnt += 1
        if cnt>=K:
            ans = max(ans, bin(i).count("1"))
    print(ans)

if __name__ == '__main__':
    main()