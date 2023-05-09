def main():
    #input
    N = int(input())
    S = input()
    Q = int(input())
    T = [0]*Q
    A = [0]*Q
    B = [0]*Q
    for i in range(Q):
        T[i],A[i],B[i] = map(int,input().split())
    
    #processing
    s1 = S[:N]
    s2 = S[N:]
    for i in range(Q):
        if T[i] == 1:
            if A[i] <= N:
                if B[i] <= N:
                    s1 = s1[:A[i]-1] + s1[B[i]-1] + s1[A[i]:B[i]-1] + s1[A[i]-1] + s1[B[i]:]
                else:
                    s1 = s1[:A[i]-1] + s2[B[i]-N-1] + s1[A[i]:B[i]-N-1] + s1[A[i]-1] + s1[B[i]-N:]
                    s2 = s2[:B[i]-N-1] + s1[A[i]-1] + s2[A[i]:B[i]-N-1] + s2[B[i]-N-1] + s2[B[i]-N:]
            else:
                if B[i] <= N:
                    s2 = s2[:A[i]-N-1] + s1[B[i]-1] + s2[A[i]-N:B[i]-1] + s2[A[i]-N-1] + s2[B[i]:]
                    s1 = s1[:B[i]-1] + s2[A[i]-N-1] + s1[A[i]:B[i]-1] + s1[B[i]-1] + s1[B[i]:]
                else:
                    s2 = s2[:A[i]-N-1] + s2[B[i]-N-1] + s2[A[i]-N:B[i]-N-1] + s2[A[i]-N-1] + s2[B[i]-N:]
        else:
            s1,s2 = s2,s1
    
    #output
    print(s1+s2)
