def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = []
    A = []
    B = []
    for i in range(Q):
        t,a,b = map(int,input().split())
        T.append(t)
        A.append(a)
        B.append(b)
    #print(N,S,Q,T,A,B)
    for i in range(Q):
        if T[i] == 1:
            a = A[i] - 1
            b = B[i] - 1
            #print("a,b",a,b)
            s = list(S)
            #print(s)
            s[a],s[b] = s[b],s[a]
            S = "".join(s)
            #print(S)
        elif T[i] == 2:
            #print("2")
            s = list(S)
            s[:N],s[N:] = s[N:],s[:N]
            S = "".join(s)
            #print(S)
    print(S)
main()
