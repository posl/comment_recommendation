def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(1, 10**5+1):
        l = 0
        r = 0
        tmp = 0
        while r < N:
            if A[r] < x:
                if r == l:
                    r += 1
                    l += 1
                else:
                    tmp -= A[l]
                    l += 1
            else:
                tmp += A[r]
                r += 1
            if tmp >= x:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()