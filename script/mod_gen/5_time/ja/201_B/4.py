def main():
    N = int(input())
    T = []
    S = []
    for i in range(N):
        s, t = input().split()
        T.append(int(t))
        S.append(s)
    T2 = sorted(T, reverse=True)
    print(S[T.index(T2[1])])

if __name__ == '__main__':
    main()