def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n - k):
        if a[i] > a[i + k]:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    solve()