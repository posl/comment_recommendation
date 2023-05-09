def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    T_max = max(T)
    T_max_index = T.index(T_max)
    S_max = S[T_max_index]
    S_max_index = []
    for i in range(N):
        if S[i] == S_max:
            S_max_index.append(i)
    if len(S_max_index) == 1:
        print(S_max_index[0] + 1)
    else:
        T_max_index = []
        for i in range(len(S_max_index)):
            T_max_index.append(T.index(T[S_max_index[i]]))
        print(min(T_max_index) + 1)

if __name__ == '__main__':
    main()