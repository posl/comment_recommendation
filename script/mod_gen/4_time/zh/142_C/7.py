def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        ans.insert(a[i]-1, i+1)
    print(*ans)

if __name__ == '__main__':
    solve()