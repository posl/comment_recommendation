def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S_i, T_i = input().split()
        S.append(S_i)
        T.append(int(T_i))
    max1 = max(T)
    max2 = 0
    for i in range(N):
        if T[i] != max1:
            max2 = max(max2, T[i])
    for i in range(N):
        if T[i] == max2:
            print(S[i])

if __name__ == '__main__':
    main()