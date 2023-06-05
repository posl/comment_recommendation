def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = []
    A = []
    B = []
    for i in range(Q):
        t,a,b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)
    #print("N = ",N)
    #print("S = ",S)
    #print("Q = ",Q)
    #print("T = ",T)
    #print("A = ",A)
    #print("B = ",B)
    for i in range(Q):
        if T[i] == 1:
            #print("交换S的第A_i个和第B_i个字符")
            s = S[A[i]-1]
            S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + s + S[B[i]:]
        else:
            #print("交换S的前N个字符和后N个字符")
            S = S[N:] + S[:N]
        #print("S = ",S)
    print(S)
