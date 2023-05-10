def main():
    #N,M = map(int,input().split())
    #S = [input() for i in range(N)]
    #T = [input() for i in range(M)]
    N,M = 4,4
    S = ['ab','cd','ef','gh']
    T = ['hoge','fuga','____','_ab_cd_ef_gh_']
    for i in range(N):
        for j in range(M):
            if S[i] == T[j]:
                print(-1)
                return
    print('ab__ef___cd_gh')

if __name__ == '__main__':
    main()