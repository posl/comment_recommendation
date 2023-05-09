def main():
    N = int(input())
    A = list(map(int,input().split()))
    X = int(input())
    sumA = sum(A)
    k = (X // sumA) * N
    X -= (X // sumA) * sumA
    sumA = 0
    for i in range(N):
        sumA += A[i]
        k += 1
        if sumA > X:
            print(k)
            exit()

if __name__ == '__main__':
    main()