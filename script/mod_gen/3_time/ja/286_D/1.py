def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    for i in range(N):
        for j in range(B[i]):
            X -= A[i]
            if X == 0:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()