def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(M):
        ans += A[i] * (i+1)
    tmp = ans
    for i in range(N-M):
        tmp -= A[i]
        tmp += A[i+M]
        ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()