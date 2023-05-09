def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(1, max(A)+1):
        l = 0
        r = 0
        while r < N:
            while r < N and A[r] >= x:
                r += 1
            ans = max(ans, x * (r - l))
            while r < N and A[r] < x:
                r += 1
            l = r
    print(ans)

if __name__ == '__main__':
    main()