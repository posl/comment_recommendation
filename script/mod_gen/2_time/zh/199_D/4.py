def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = []
    A = []
    B = []
    for i in range(Q):
        t, a, b = input().split()
        T.append(int(t))
        A.append(int(a))
        B.append(int(b))
    for i in range(Q):
        if T[i] == 1:
            S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + S[A[i]-1] + S[B[i]:]
        else:
            S = S[N:] + S[:N]
    print(S)

if __name__ == '__main__':
    main()