def main():
    N,M = map(int,input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
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
            if check(s + S[i]):
                ret = dfs(s + S[i])
                if ret != None:
                    return ret
        return None
    print(dfs(''))

if __name__ == '__main__':
    main()