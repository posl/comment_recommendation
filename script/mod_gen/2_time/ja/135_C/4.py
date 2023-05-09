def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    ans = 0
    for i in range(N):
        ans += min(A[i], B[i])
        B[i] -= min(A[i], B[i])
        ans += min(A[i+1], B[i])
        A[i+1] -= min(A[i+1], B[i])
    print(ans)

if __name__ == '__main__':
    main()