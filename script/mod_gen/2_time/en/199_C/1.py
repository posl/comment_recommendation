def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = [0]*Q
    A = [0]*Q
    B = [0]*Q
    for i in range(Q):
        T[i], A[i], B[i] = map(int, input().split())
    S = list(S)
    swap = False
    for i in range(Q):
        if T[i] == 1:
            if swap:
                A[i] = (A[i] - 1 + N) % (2*N) + 1
                B[i] = (B[i] - 1 + N) % (2*N) + 1
            A[i] -= 1
            B[i] -= 1
            S[A[i]], S[B[i]] = S[B[i]], S[A[i]]
        else:
            swap = not swap
    if swap:
        S = S[N:] + S[:N]
    print(''.join(S))

if __name__ == '__main__':
    main()