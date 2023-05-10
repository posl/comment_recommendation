def main():
    S = input()
    Q = int(input())
    T = [0]*Q
    F = [0]*Q
    C = ['']*Q
    for i in range(Q):
        T[i] = input()
        if T[i] == '1':
            continue
        else:
            F[i], C[i] = input().split()
            F[i] = int(F[i])
    S = list(S)
    reverse = 0
    for i in range(Q):
        if T[i] == '1':
            reverse = 1 - reverse
        else:
            if F[i] == 1:
                if reverse == 0:
                    S.insert(0, C[i])
                else:
                    S.append(C[i])
            else:
                if reverse == 0:
                    S.append(C[i])
                else:
                    S.insert(0, C[i])
    if reverse == 0:
        print(''.join(S))
    else:
        S = S[::-1]
        print(''.join(S))

if __name__ == '__main__':
    main()