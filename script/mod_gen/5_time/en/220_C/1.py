def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    s = sum(A)
    k = (X // s) * N
    X = X % s
    for i in range(N):
        X -= A[i]
        k += 1
        if X < 0:
            break
    print(k)

if __name__ == '__main__':
    main()