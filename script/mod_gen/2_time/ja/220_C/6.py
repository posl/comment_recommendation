def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    sumA = sum(A)
    count = 0
    if X <= sumA:
        for i in range(N):
            count += 1
            if sumA >= X:
                break
            sumA += A[i]
    else:
        count = N * (X // sumA)
        sumA = sumA * (X // sumA)
        for i in range(N):
            count += 1
            if sumA >= X:
                break
            sumA += A[i]
    print(count)
    return

if __name__ == '__main__':
    main()