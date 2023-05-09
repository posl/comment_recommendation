def main():
    S = input()
    Q = int(input())
    T = []
    F = []
    C = []
    for i in range(Q):
        t = input().split()
        T.append(int(t[0]))
        if len(t) == 3:
            F.append(int(t[1]))
            C.append(t[2])
    #print(T)
    #print(F)
    #print(C)
    A = list(S)
    #print(A)
    reverse = False
    for i in range(Q):
        if T[i] == 1:
            reverse = not reverse
        else:
            if reverse:
                if F[i] == 1:
                    A.append(C[i])
                else:
                    A.insert(0, C[i])
            else:
                if F[i] == 1:
                    A.insert(0, C[i])
                else:
                    A.append(C[i])
    if reverse:
        A.reverse()
    print(''.join(A))

if __name__ == '__main__':
    main()