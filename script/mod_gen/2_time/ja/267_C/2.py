def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-M+1):
        ans += sum(A[i:i+M]) * (M-i)
    print(ans)

if __name__ == '__main__':
    main()