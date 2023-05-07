def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(1, 10 ** 5 + 1):
        l = 0
        r = 0
        cnt = 0
        while r < N:
            if A[r] >= x:
                r += 1
                cnt += 1
            else:
                ans = max(ans, x * cnt)
                while l < r:
                    if A[l] >= x:
                        l += 1
                        cnt -= 1
                    else:
                        l += 1
                        break
    print(max(ans, x * cnt))

if __name__ == '__main__':
    main()