def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] >= i+1:
            ans += A[i] - (i+1)
        else:
            ans += A[i]
    print(ans)

if __name__ == '__main__':
    main()