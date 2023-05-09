def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    T.sort(reverse=True)
    print(S[T.index(T[1])])

if __name__ == '__main__':
    main()