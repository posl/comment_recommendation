def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if m > n:
        print("No")
        return
    a.sort()
    b.sort()
    for i in range(m):
        if a[n - i - 1] < b[m - i - 1]:
            print("No")
            return
    print("Yes")
main()
