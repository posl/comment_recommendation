def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-1):
        ans += A[i] * (N-1-i) * 2
    print(ans)

if __name__ == '__main__':
    main()