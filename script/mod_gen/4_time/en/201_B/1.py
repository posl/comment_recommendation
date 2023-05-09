def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    T_max = max(T)
    for i in range(N):
        if T[i] == T_max:
            T[i] = 0
    T_second = max(T)
    for i in range(N):
        if T[i] == T_second:
            print(S[i])
            break

if __name__ == '__main__':
    main()