def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    T_max = max(T)
    T.pop(T.index(T_max))
    S.pop(T.index(T_max))
    print(S[T.index(max(T))])

if __name__ == '__main__':
    main()