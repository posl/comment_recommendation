def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        if A[i] < 0:
            A[i] *= -1
        if A[i+1] < 0:
            A[i+1] *= -1
        ans += A[i+1] - A[i]
    print(ans)

if __name__ == '__main__':
    main()