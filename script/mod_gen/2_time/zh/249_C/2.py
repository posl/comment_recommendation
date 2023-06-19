def main():
    N,K = map(int,input().split())
    S = []
    for i in range(N):
        S.append(input())
    ans = 0
    for i in range(2**N):
        cnt = 0
        tmp = []
        for j in range(N):
            if i&(1<<j):
                tmp.append(S[j])
                cnt += 1
        if cnt != K:
            continue
        ans = max(ans,len(set("".join(tmp))))
    print(ans)

if __name__ == '__main__':
    main()