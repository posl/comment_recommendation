def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = 0
    for i in range(n-1):
        if a[i] > 2*a[i+1]:
            ans = i+1
    print(n-ans)

if __name__ == '__main__':
    solve()