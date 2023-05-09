def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s,t = map(str,input().split())
        S.append(s)
        T.append(t)
    S_set = set(S)
    T_set = set(T)
    if len(S_set) == len(T_set):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()