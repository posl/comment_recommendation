def main():
    N, M = map(int, input().split())
    P = [0] * M
    Y = [0] * M
    for i in range(M):
        P[i], Y[i] = map(int, input().split())
    #print(P)
    #print(Y)
    Y2 = sorted(Y)
    #print(Y2)
    #print(Y2.index(32))
    #print(Y2.index(12))
    #print(Y2.index(63))
    #print(Y2.index(55))
    #print(Y2.index(77))
    #print(Y2.index(99))
    for i in range(M):
        print(str(P[i]).zfill(6) + str(Y2.index(Y[i]) + 1).zfill(6))

if __name__ == '__main__':
    main()