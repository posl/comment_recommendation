def main():
    S = input()
    Q = int(input())
    T = []
    F = []
    C = []
    for i in range(Q):
        t = list(map(str, input().split()))
        T.append(t[0])
        if len(t) == 3:
            F.append(t[1])
            C.append(t[2])
    a = []
    b = []
    for i in range(Q):
        if T[i] == "1":
            a, b = b, a
        else:
            if F[i] == "1":
                a.append(C[i])
            else:
                b.append(C[i])
    S = "".join(a[::-1]) + S + "".join(b)
    print(S)

if __name__ == '__main__':
    main()