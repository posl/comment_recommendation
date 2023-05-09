def main():
    N, Q = map(int, input().split())
    S = input()
    T = []
    for i in range(Q):
        t, x = map(int, input().split())
        T.append([t, x])
    S = S[::-1]
    for i in range(Q):
        if T[i][0] == 1:
            S = S[:T[i][1]] + S[T[i][1]+1:] + S[T[i][1]]
        else:
            print(S[T[i][1]-1])

if __name__ == '__main__':
    main()