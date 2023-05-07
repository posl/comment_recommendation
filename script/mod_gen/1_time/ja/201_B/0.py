def main():
    N = int(input())
    S = [None] * N
    T = [None] * N
    for i in range(N):
        S[i], T[i] = input().split()
        T[i] = int(T[i])
    T2 = sorted(T, reverse=True)
    for i in range(N):
        if T[i] == T2[1]:
            print(S[i])
            return

if __name__ == '__main__':
    main()