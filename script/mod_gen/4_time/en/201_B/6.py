def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(input().split()[0])
        T.append(int(input().split()[1]))
    T.sort()
    for i in range(N):
        if T[N-2] == int(input().split()[1]):
            print(S[i])
            break

if __name__ == '__main__':
    main()