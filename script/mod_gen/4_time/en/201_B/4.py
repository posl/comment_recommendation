def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S_i, T_i = input().split()
        S.append(S_i)
        T.append(int(T_i))
    max = 0
    second = 0
    index = 0
    for i in range(N):
        if max < T[i]:
            max = T[i]
            index = i
    for i in range(N):
        if second < T[i] and i != index:
            second = T[i]
    print(S[index])

if __name__ == '__main__':
    main()