def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = A[0] - 1
    for i in range(1, N):
        ans += A[i]
    print(ans)

if __name__ == '__main__':
    main()