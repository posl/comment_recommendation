def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    max_d = 0
    for i in range(N):
        if i == 0:
            max_d = K - A[N-1] + A[0]
        else:
            max_d = max(max_d, A[i]-A[i-1])
    print(K-max_d)

if __name__ == '__main__':
    main()