def main():
    S = input()
    Q = int(input())
    T = []
    K = []
    for i in range(Q):
        t, k = map(int, input().split())
        T.append(t)
        K.append(k)
    S0 = S
    S1 = S0.replace('A', 'D').replace('B', 'E').replace('C', 'F')
    S2 = S1.replace('D', 'E').replace('E', 'F').replace('F', 'D')
    S3 = S2.replace('D', 'F').replace('E', 'D').replace('F', 'E')
    for i in range(Q):
        t = T[i]
        k = K[i]
        if t % 3 == 0:
            print(S0[k - 1])
        elif t % 3 == 1:
            print(S1[k - 1])
        elif t % 3 == 2:
            print(S2[k - 1])
        else:
            print(S3[k - 1])

if __name__ == '__main__':
    main()