def main():
    N, K = map(int, input().split())
    A = [0] * N
    for i in range(K):
        d = int(input())
        A_i = list(map(int, input().split()))
        for j in range(d):
            A[A_i[j] - 1] += 1
    print(A.count(0))

if __name__ == '__main__':
    main()