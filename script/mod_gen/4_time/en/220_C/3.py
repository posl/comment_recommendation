def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    sumA = sum(A)
    n = X // sumA
    x = X % sumA
    sumB = 0
    for i in range(N):
        sumB += A[i]
        if sumB > x:
            print(n * N + i + 1)
            break

if __name__ == '__main__':
    main()