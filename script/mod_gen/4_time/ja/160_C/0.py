def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    ans = K - (A[-1] - A[0])
    for i in range(N-1):
        ans = max(ans, A[i+1] - A[i])
    print(K - ans)
    return

if __name__ == '__main__':
    main()