def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    S = [K-Q for _ in range(N)]
    for i in range(Q):
        S[A[i]-1] += 1
    for i in range(N):
        if S[i] > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()