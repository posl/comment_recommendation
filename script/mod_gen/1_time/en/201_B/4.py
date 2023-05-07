def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    T_sort = sorted(T, reverse=True)
    print(S[T.index(T_sort[1])])

if __name__ == '__main__':
    main()