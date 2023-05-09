def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(1, 100001):
        l = 0
        r = 0
        for i in range(N):
            while r < N and A[r] >= x:
                r += 1
            ans = max(ans, x * (r - l))
            if A[i] >= x:
                l += 1
    print(ans)

if __name__ == '__main__':
    main()