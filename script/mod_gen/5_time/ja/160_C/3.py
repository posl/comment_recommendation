def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    ans = K + min(A[0] + K - A[-1], *[A[i] - A[i-1] for i in range(1, N)])
    print(ans)

if __name__ == '__main__':
    main()