def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = []
    for i in range(N):
        B.append(A[i] - (i+1))
    B.sort()
    if N % 2 == 0:
        b = (B[N//2] + B[N//2-1]) // 2
    else:
        b = B[N//2]
    ans = 0
    for i in range(N):
        ans += abs(A[i] - (b+i+1))
    print(ans)

if __name__ == '__main__':
    main()