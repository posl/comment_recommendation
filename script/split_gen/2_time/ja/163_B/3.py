def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(m):
        n -= a[i]
        if n < 0:
            print(i)
            return
    print(n)
