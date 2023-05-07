def main():
    S = input()
    Q = int(input())
    T = []
    F = []
    C = []
    for i in range(Q):
        T.append(list(map(str, input().split())))
        if len(T[i]) == 2:
            F.append(T[i][0])
            C.append(T[i][1])
    if F.count('1') % 2 == 0:
        S = S[::-1]
    S = S.replace(' ', '')
    for i in range(Q):
        if len(T[i]) == 1:
            S = S[::-1]
        else:
            if F[i] == '1':
                S = C[i] + S
            else:
                S = S + C[i]
    print(S)
