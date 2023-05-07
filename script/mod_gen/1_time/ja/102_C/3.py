def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [A[i] - i for i in range(N)]
    A.sort()
    b = A[N//2]
    ans = 0
    for i in range(N):
        ans += abs(A[i] - b)
    print(ans)

if __name__ == '__main__':
    main()