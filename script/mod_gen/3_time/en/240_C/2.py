def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    for i in range(N):
        if A[i] <= X:
            X = B[i]
        elif B[i] <= X:
            X = A[i]
    if X == 0:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()