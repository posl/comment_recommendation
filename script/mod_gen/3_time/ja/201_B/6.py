def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(input().split()[0])
        T.append(int(input().split()[1]))
    print(S[T.index(sorted(T)[-2])])

if __name__ == '__main__':
    main()