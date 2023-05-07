def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = N
    for i in range(K):
        ans -= (ans % A[i])
    print(ans)

if __name__ == '__main__':
    main()