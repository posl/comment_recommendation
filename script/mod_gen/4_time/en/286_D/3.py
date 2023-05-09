def main():
    N, X = map(int, input().split())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    sum = 0
    for i in range(N):
        sum += A[i] * B[i]
    if sum >= X:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()