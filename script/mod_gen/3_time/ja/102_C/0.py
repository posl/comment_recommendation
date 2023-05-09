def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    b = A[N//2]
    ans = 0
    for i in range(N):
        ans += abs(A[i] - (b - N//2 + i))
    print(ans)

if __name__ == '__main__':
    main()