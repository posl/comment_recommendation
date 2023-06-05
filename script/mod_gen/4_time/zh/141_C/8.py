def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for i in range(Q)]
    count = [0] * N
    for i in range(Q):
        count[A[i]-1] += 1
    for i in range(N):
        if K - (Q - count[i]) > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()