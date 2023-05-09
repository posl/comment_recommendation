def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    # A = [1, 2, 3, 4]
    # K = 2
    # D = 2
    # N = 4
    A.sort(reverse=True)
    # A = [4, 3, 2, 1]
    ans = 0
    for i in range(K):
        ans += A[i]
    # ans = 7
    if ans % D == 0:
        print(ans)
    else:
        print(-1)
main()

if __name__ == '__main__':
    main()