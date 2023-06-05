def main():
    S = input()
    Q = int(input())
    T = []
    F = []
    C = []
    for i in range(Q):
        tmp = input().split(' ')
        T.append(tmp[0])
        if tmp[0] == '2':
            F.append(tmp[1])
            C.append(tmp[2])
    S = list(S)
    C.reverse()
    for i in range(Q):
        if T[i] == '1':
            S.reverse()
        else:
            if F[i] == '1':
                S.append(C[i])
            else:
                S.insert(0, C[i])
    print(''.join(S))
