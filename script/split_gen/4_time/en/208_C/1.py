def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if k <= n:
        for i in range(n):
            print(k)
        return
    else:
        k -= n
        for i in range(n):
            if a[i] <= k // n + ((k % n) > i):
                print(a[i] + k // n + ((k % n) > i))
            else:
                print(a[i])
        return
