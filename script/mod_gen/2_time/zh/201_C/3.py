def second_height():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(input().split()[0])
        T.append(int(input().split()[1]))
    T_sort = sorted(T)
    for i in range(N):
        if T[i] == T_sort[-2]:
            print(S[i])
            break

if __name__ == '__main__':
    second_height()