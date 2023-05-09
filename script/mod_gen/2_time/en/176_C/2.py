def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if i == 0:
            ans += A[i]
        else:
            if A[i] > A[i-1]:
                ans += A[i] - A[i-1]
    print(ans)

if __name__ == '__main__':
    main()