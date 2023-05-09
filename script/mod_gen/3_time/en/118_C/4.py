def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    for i in range(n-1):
        a[i+1] = a[i] - a[i+1]
    print(a[-1])

if __name__ == '__main__':
    solve()