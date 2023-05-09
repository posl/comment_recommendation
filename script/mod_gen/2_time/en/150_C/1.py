def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    Q = [int(x) for x in input().split()]
    a = P.index(1)
    b = Q.index(1)
    for i in range(N):
        if P[i] > P[a]:
            a += 1
        if Q[i] > Q[b]:
            b += 1
    print(abs(a - b))

if __name__ == '__main__':
    main()