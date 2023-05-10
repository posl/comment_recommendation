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
    l = list(S)
    for i in range(Q):
        if T[i] == 1:
            l[A[i]-1], l[B[i]-1] = l[B[i]-1], l[A[i]-1]
        else:
            l[0:N], l[N:2*N] = l[N:2*N], l[0:N]
    print("".join(l))
