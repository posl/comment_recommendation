def main():
    S = input()
    Q = int(input())
    T = []
    K = []
    for i in range(Q):
        t, k = map(int, input().split())
        T.append(t)
        K.append(k)
    A = S.count("A")
    B = S.count("B")
    C = S.count("C")
    for i in range(Q):
        t = T[i]
        k = K[i]
        if t == 0:
            print(S[k-1])
        else:
            t %= 3
            if t == 1:
                if k <= A:
                    print("A")
                elif k <= A+B:
                    print("B")
                else:
                    print("C")
            elif t == 2:
                if k <= B:
                    print("B")
                elif k <= A+B:
                    print("C")
                else:
                    print("A")
            else:
                if k <= C:
                    print("C")
                elif k <= A+C:
                    print("A")
                else:
                    print("B")
main()

if __name__ == '__main__':
    main()