def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for x in range(1, 1001):
        for i in range(n):
            if x < a[i] or b[i] < x:
                break
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()