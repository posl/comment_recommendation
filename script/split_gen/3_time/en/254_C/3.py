def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(a)
    d = {}
    for i in range(n):
        d[b[i]] = i
    for i in range(n):
        a[i] = d[a[i]]
    for i in range(n):
        if a[i] - i > k:
            print("No")
            return
    print("Yes")
