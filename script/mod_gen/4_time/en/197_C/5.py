def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(30):
        bit = 1 << i
        cnt = 0
        for j in range(n):
            if a[j] & bit:
                cnt += 1
        ans |= bit * (cnt % 2)
    print(ans)

if __name__ == '__main__':
    solve()