def main():
    S = input()
    Q = int(input())
    T = []
    F = []
    C = []
    for i in range(Q):
        t = input()
        if t == "1":
            T.append(1)
        else:
            f, c = t.split()
            T.append(2)
            F.append(int(f))
            C.append(c)
    rev = 0
    ans = []
    for i in range(Q):
        if T[i] == 1:
            rev ^= 1
        else:
            if (rev + F[i]) % 2 == 0:
                ans.append(C[i])
            else:
                ans.insert(0, C[i])
    if rev == 0:
        print("".join(ans) + S)
    else:
        print("".join(ans[::-1]) + S[::-1])

if __name__ == '__main__':
    main()