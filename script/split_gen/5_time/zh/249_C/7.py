def main():
    N,K = map(int,input().split())
    S = [input() for _ in range(N)]
    S.sort(key = lambda x: len(x))
    ans = 0
    for i in range(1<<N):
        if bin(i).count('1') != K:
            continue
        else:
            tmp = []
            for j in range(N):
                if i & (1<<j):
                    tmp.append(S[j])
            tmp = ''.join(tmp)
            if len(set(tmp)) == K:
                ans = max(ans,len(tmp))
    print(ans)
