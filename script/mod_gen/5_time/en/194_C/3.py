def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N - 1):
        ans += (A[i + 1] - A[i]) ** 2
    print(ans)

if __name__ == '__main__':
    main()