def main():
    N,K = map(int,input().split())
    S = []
    for i in range(N):
        S.append(input())
    ans = 0
    for i in range(2**N):
        T = []
        for j in range(N):
            if (i>>j)&1:
                T.append(S[j])
        if len(T)!=K:
            continue
        cnt = 0
        for j in range(26):
            flag = False
            for k in range(K):
                if chr(ord('a')+j) in T[k]:
                    flag = True
            if flag:
                cnt+=1
        if cnt==K:
            ans = max(ans,K)
    print(ans)
