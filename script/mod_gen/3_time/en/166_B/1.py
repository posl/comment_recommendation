def main():
    N, K = map(int, input().split())
    D = [0] * N
    for i in range(K):
        d = int(input())
        A = list(map(int, input().split()))
        for j in range(d):
            D[A[j] - 1] = 1
    print(D.count(0))

if __name__ == '__main__':
    main()