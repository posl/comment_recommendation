def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    ans = 0
    for i in range(N):
        ans += min(A[i], B[i])
        if A[i] < B[i]:
            B[i] = B[i] - A[i]
            ans += min(A[i+1], B[i])
            A[i+1] = max(0, A[i+1] - B[i])
    print(ans)
main()

if __name__ == '__main__':
    main()