def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(40, -1, -1):
        tmp = 0
        for a in A:
            if a & (1 << i):
                tmp += a ^ (1 << i)
            else:
                tmp += a
        if tmp <= k:
            ans += 1 << i
    print(ans)

if __name__ == '__main__':
    main()