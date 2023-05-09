def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = float('inf')
    for i in range(N):
        ans = min(ans, abs(A[i] - (i + 1)))
    print(ans)

if __name__ == '__main__':
    main()