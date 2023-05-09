def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * M
    for i in range(M):
        B[i] = sum(A[i:N-M+i+1])
    B.sort(reverse=True)
    ans = 0
    for i in range(M):
        ans += (i+1) * B[i]
    print(ans)

if __name__ == '__main__':
    main()