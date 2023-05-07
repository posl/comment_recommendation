def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(input().split()[0])
        T.append(int(input().split()[1]))
    for i in range(N):
        if S[i] in S[:i]:
            T[i] = -1
    print(T.index(max(T)))

if __name__ == '__main__':
    main()