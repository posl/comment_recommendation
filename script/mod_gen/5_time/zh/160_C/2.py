def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(K)
    ans = K
    for i in range(N):
        ans = min(ans, K - A[i] + A[i - 1])
    print(ans)
    return

if __name__ == '__main__':
    main()