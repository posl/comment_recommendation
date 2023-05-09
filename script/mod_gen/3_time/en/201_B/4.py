def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    # print(S)
    # print(T)
    max = T[0]
    max_idx = 0
    for i in range(1, N):
        if T[i] > max:
            max = T[i]
            max_idx = i
    # print(max, max_idx)
    max = T[0]
    for i in range(0, N):
        if T[i] > max and i != max_idx:
            max = T[i]
    # print(max)
    for i in range(0, N):
        if T[i] == max:
            print(S[i])

if __name__ == '__main__':
    main()