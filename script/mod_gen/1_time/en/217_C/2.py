def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    Q = [0] * N
    for i in range(N):
        Q[P[i] - 1] = i + 1
    print(*Q)

if __name__ == '__main__':
    main()