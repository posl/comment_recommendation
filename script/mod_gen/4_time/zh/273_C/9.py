def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * n
    for i in range(n):
        if i == 0:
            ans[i] = 1
        else:
            if a[i] == a[i-1]:
                ans[i] = ans[i-1]
            else:
                ans[i] = ans[i-1] + 1
    for i in range(n):
        print(ans[ans[i]-1])

if __name__ == '__main__':
    solve()