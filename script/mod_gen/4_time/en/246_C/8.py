def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N):
        if A[i] <= X:
            K -= 1
            A[i] = 0
        else:
            break
    if K <= 0:
        print(sum(A))
    else:
        A = [max(a - K * X, 0) for a in A]
        print(sum(A))

if __name__ == '__main__':
    main()