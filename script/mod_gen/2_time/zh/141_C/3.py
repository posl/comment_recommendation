def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for i in range(Q)]
    P = [K-Q for i in range(N)]
    for i in A:
        P[i-1] += 1
    for i in P:
        if i > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()