def main():
    N,K,Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    scores = [0] * N
    for i in range(Q):
        scores[A[i]-1] += 1
    for i in range(N):
        if K - (Q - scores[i]) > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()