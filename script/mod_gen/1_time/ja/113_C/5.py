def main():
    N, M = map(int, input().split())
    Y = [0] * (N + 1)
    for m in range(M):
        P, Y = map(int, input().split())
        Y[P] += 1
        print(str(P).zfill(6) + str(Y[P]).zfill(6))

if __name__ == '__main__':
    main()