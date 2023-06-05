def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = sum(a)
    if a[m-1] >= total/(4*m):
        print("是")
    else:
        print("否")

if __name__ == '__main__':
    solve()