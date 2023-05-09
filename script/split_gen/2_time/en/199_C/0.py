def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = [0] * Q
    A = [0] * Q
    B = [0] * Q
    for i in range(Q):
        T[i], A[i], B[i] = map(int, input().split())
    S = list(S)
    #print(S)
    flip = False
    for i in range(Q):
        if T[i] == 1:
            if flip:
                if A[i] > N:
                    A[i] -= N
                else:
                    A[i] += N
                if B[i] > N:
                    B[i] -= N
                else:
                    B[i] += N
            A[i] -= 1
            B[i] -= 1
            S[A[i]], S[B[i]] = S[B[i]], S[A[i]]
        else:
            flip = not flip
    if flip:
        S = S[N:] + S[:N]
    print(''.join(S))
