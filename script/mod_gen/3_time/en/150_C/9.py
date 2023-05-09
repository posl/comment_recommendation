def main():
    N = int(input())
    P = tuple(map(int, input().split()))
    Q = tuple(map(int, input().split()))
    P = P[0] * 10 ** (N * 2) + P[1] * 10 ** N + P[2]
    Q = Q[0] * 10 ** (N * 2) + Q[1] * 10 ** N + Q[2]
    #print(P, Q)
    P, Q = sorted((P, Q))
    #print(P, Q)
    a = 0
    for i in range(1, N + 1):
        a += (i - 1) * (N - i + 1) * (N - i + 1) * 10 ** (N - i) * (i - 1)
        #print(a)
        for j in range(1, i):
            a += 10 ** (N - i) * (i - j)
            #print(a)
        for j in range(i + 1, N + 1):
            a += 10 ** (N - i) * (N - i - j + 1)
            #print(a)
    b = 0
    for i in range(1, N + 1):
        b += (i - 1) * (N - i + 1) * (N - i + 1) * 10 ** (N - i) * (i - 1)
        #print(b)
        for j in range(1, i):
            b += 10 ** (N - i) * (i - j)
            #print(b)
        for j in range(i + 1, N + 1):
            b += 10 ** (N - i) * (N - i - j + 1)
            #print(b)
    print(abs(a - b))

if __name__ == '__main__':
    main()