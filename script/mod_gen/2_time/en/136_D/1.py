def main():
    S = input()
    N = len(S)
    L = [0] * N
    R = [0] * N
    for i in range(N):
        if S[i] == 'L':
            L[i] = 1
        else:
            R[i] = 1
    for i in range(1, N):
        L[i] += L[i - 1]
    for i in reversed(range(N - 1)):
        R[i] += R[i + 1]
    for i in range(N):
        if S[i] == 'L':
            print((R[i] + 1) // 2, end=' ')
        else:
            print((L[i] + 1) // 2, end=' ')
    print()

if __name__ == '__main__':
    main()