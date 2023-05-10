def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    #print(N)
    #print(S)
    #print(T)
    #S_1 S_2 ... S_N
    #T_1 T_2 ... T_N
    for i in range(N):
        if i == 0:
            continue
        if T[i] <= T[i-1]:
            T[i] = T[i-1] + S[i-1]
    print(*T, sep='\n')

if __name__ == '__main__':
    main()