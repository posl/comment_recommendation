def main():
    N, K, Q = map(int, input().split())
    A = [0] * N
    for i in range(Q):
        A[int(input()) - 1] += 1
    for i in range(N):
        if K - (Q - A[i]) > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()