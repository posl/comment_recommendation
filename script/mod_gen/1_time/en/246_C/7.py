def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    print(sum([max(A[i] - X * K, 0) for i in range(N)]))

if __name__ == '__main__':
    main()