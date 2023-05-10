def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    T.sort(reverse=True)
    for i in range(N):
        if T[1] == int(T[i]):
            print(S[i])
            break

if __name__ == '__main__':
    main()