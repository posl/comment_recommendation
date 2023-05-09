def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    ans[0] = sum(A)
    for i in range(N-1):
        ans[i+1] = A[i] * 2 - ans[i]
    print(*ans)

if __name__ == '__main__':
    main()