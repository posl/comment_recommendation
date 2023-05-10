def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    sumA = sum(A)
    k = X//sumA
    sumB = sumA*k
    for i in range(N):
        sumB += A[i]
        k += 1
        if sumB > X:
            break
    print(k)

if __name__ == '__main__':
    main()