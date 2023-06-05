def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N):
        A[i] -= i
    A.sort()
    if N % 2 == 1:
        b = A[N // 2]
    else:
        b = (A[N // 2] + A[N // 2 - 1]) // 2
    ans = 0
    for i in range(N):
        ans += abs(A[i] - b)
    print(ans)

if __name__ == '__main__':
    main()