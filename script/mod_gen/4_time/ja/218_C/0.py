def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        T.append(input())
    #print(S)
    #print(T)
    S1 = []
    S2 = []
    S3 = []
    S4 = []
    T1 = []
    T2 = []
    T3 = []
    T4 = []
    #S1
    for i in range(N):
        S1.append(S[i][::-1])
    #S2
    for i in range(N):
        S2.append(S1[i][::-1])
    #S3
    for i in range(N):
        S3.append(S2[i][::-1])
    #S4
    for i in range(N):
        S4.append(S3[i][::-1])
    #T1
    for i in range(N):
        T1.append(T[i][::-1])
    #T2
    for i in range(N):
        T2.append(T1[i][::-1])
    #T3
    for i in range(N):
        T3.append(T2[i][::-1])
    #T4
    for i in range(N):
        T4.append(T3[i][::-1])
    #print(S1)
    #print(S2)
    #print(S3)
    #print(S4)
    #print(T1)
    #print(T2)
    #print(T3)
    #print(T4)
    if S1 == T or S2 == T or S3 == T or S4 == T:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()