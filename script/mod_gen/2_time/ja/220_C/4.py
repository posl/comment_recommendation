def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    sumA = sum(A)
    if X < sumA:
        print(0)
        return
    k = (X // sumA) * N
    X -= (X // sumA) * sumA
    for i in range(N):
        if X < 0:
            break
        X -= A[i]
        k += 1
    print(k)
main()

if __name__ == '__main__':
    main()