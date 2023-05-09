def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S_i, T_i = input().split()
        S.append(S_i)
        T.append(int(T_i))
    max_T = max(T)
    max_T_index = T.index(max_T)
    T[max_T_index] = 0
    max_T = max(T)
    print(S[T.index(max_T)])

if __name__ == '__main__':
    main()