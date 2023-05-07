def main():
    S = input()
    N = len(S)
    L = [0] * N
    R = [0] * N
    for i in range(N):
        if S[i] == 'R':
            R[i] = 1
        else:
            L[i] = 1
    for i in range(N):
        if i == N - 1:
            print(L[i], end = '')
        else:
            print(L[i], end = ' ')
    print()
    for i in range(N - 1):
        if i == N - 2:
            print(R[i], end = '')
        else:
            print(R[i], end = ' ')
    print()
    for i in range(N - 2, -1, -1):
        if i == 0:
            print(L[i], end = '')
        else:
            print(L[i], end = ' ')
    print()
    for i in range(N - 1):
        if i == N - 2:
            print(R[i], end = '')
        else:
            print(R[i], end = ' ')
    print()
    for i in range(N):
        if i == N - 1:
            print(L[i], end = '')
        else:
            print(L[i], end = ' ')
    print()

if __name__ == '__main__':
    main()