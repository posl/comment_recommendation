def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = []
    A = []
    B = []
    for i in range(Q):
        t, a, b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)
    # swap 1st half and 2nd half
    swap = False
    
    for i in range(Q):
        if T[i] == 1:
            if swap:
                a = A[i] - N
                b = B[i] - N
                if a < 0:
                    a += 2*N
                if b < 0:
                    b += 2*N
                A[i] = a
                B[i] = b
            S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + S[A[i]-1] + S[B[i]:]
        else:
            swap = not swap
    if swap:
        print(S[N:] + S[:N])
    else:
        print(S)

if __name__ == '__main__':
    main()