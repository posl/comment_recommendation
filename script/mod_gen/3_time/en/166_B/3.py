def main():
    N, K = [int(x) for x in input().split()]
    A = [0] * N
    for i in range(K):
        d = int(input())
        a = [int(x) for x in input().split()]
        for j in range(d):
            A[a[j] - 1] = 1
    print(A.count(0))

if __name__ == '__main__':
    main()