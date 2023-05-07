def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    x = 0
    for i in range(N):
        x += A[i]
        ans = max(ans, x)
    print(ans)

if __name__ == '__main__':
    main()