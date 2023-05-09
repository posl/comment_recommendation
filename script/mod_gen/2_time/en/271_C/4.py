def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if i+1 >= a[i]:
            ans = i+1
    print(ans)

if __name__ == '__main__':
    solve()