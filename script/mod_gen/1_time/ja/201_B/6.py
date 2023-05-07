def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    T.sort()
    ans = S[T.index(T[N-2])]
    print(ans)

if __name__ == '__main__':
    main()