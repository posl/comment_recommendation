def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S_i, T_i = input().split()
        S.append(S_i)
        T.append(int(T_i))
    T_sorted = sorted(T, reverse = True)
    second_highest = T_sorted[1]
    for i in range(N):
        if T[i] == second_highest:
            print(S[i])
            break

if __name__ == '__main__':
    main()