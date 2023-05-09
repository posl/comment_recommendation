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
    #print(N)
    #print(S)
    #print(Q)
    #print(T)
    #print(A)
    #print(B)
    s1 = S[0:N]
    s2 = S[N:2*N]
    #print(s1)
    #print(s2)
    for i in range(Q):
        if T[i] == 1:
            if A[i] > N:
                A[i] -= N
            else:
                A[i] += N
            if B[i] > N:
                B[i] -= N
            else:
                B[i] += N
            #print(A[i])
            #print(B[i])
            #print(s1)
            #print(s2)
            if A[i] > B[i]:
                tmp = A[i]
                A[i] = B[i]
                B[i] = tmp
            if A[i] == 1:
                s1 = s2[B[i]-2] + s1[1:A[i]-1] + s2[A[i]-2] + s1[A[i]:N]
                s2 = s2[0:B[i]-1] + s1[B[i]-2] + s2[B[i]:N]
            else:
                s1 = s1[0:A[i]-1] + s2[A[i]-2] + s1[A[i]:N]
                s2 = s1[B[i]-2] + s2[A[i]:B[i]-1] + s1[B[i]-2] + s2[B[i]:N]
            #print(s1)
            #print(s2)
        else:
            tmp = s1
            s1 = s2
            s2 = tmp
            #print(s1)
            #print(s2)
    print(s1 + s2)
