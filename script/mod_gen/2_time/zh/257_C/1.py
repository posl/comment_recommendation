def solve():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))
    l = 0
    r = 10 ** 9 + 1
    while r - l > 1:
        mid = (l + r) // 2
        cnt = 0
        for i in range(n):
            if s[i] == '0' and w[i] >= mid:
                cnt += 1
            if s[i] == '1' and w[i] < mid:
                cnt += 1
        if cnt == n:
            l = mid
        else:
            r = mid
    print(l)

if __name__ == '__main__':
    solve()