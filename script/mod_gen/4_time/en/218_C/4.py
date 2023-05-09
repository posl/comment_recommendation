def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]
    S = [s for s in S if '#' in s]
    T = [t for t in T if '#' in t]
    if len(S) != len(T) or len(S[0]) != len(T[0]):
        print('No')
        return
    for i in range(N):
        for j in range(N):
            if S[0][0] == T[i][j]:
                if all(S[k] == T[k + i][j:j + len(S[0])] for k in range(len(S))):
                    print('Yes')
                    return
    print('No')

if __name__ == '__main__':
    main()