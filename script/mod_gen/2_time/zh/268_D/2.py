def main():
    N,M = list(map(int, input().split()))
    S = []
    for i in range(N):
        S.append(input())
    T = []
    for i in range(M):
        T.append(input())
    #print(N,M,S,T)
    def check(s):
        for t in T:
            if t in s:
                return False
        return True
    def dfs(s):
        if len(s) == N:
            return s
        for i in range(N):
            if S[i] in s:
                continue
            s.append(S[i])
            if check(s):
                res = dfs(s)
                if res:
                    return res
            s.pop()
        return None
    res = dfs([])
    if res:
        print("_".join(res))
    else:
        print(-1)

if __name__ == '__main__':
    main()