def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = [0]*(n+1)
    ans = 0
    for i in range(n):
        if a[i] != a[i-1]:
            ans += b.count(i)
            b = [0]*(n+1)
        b[a[i]] += 1
    ans += b.count(n)
    b = [0]*(n+1)
    for i in range(n):
        if a[i] != a[i-1]:
            print(ans - b.count(i))
            b = [0]*(n+1)
        b[a[i]] += 1
    print(ans - b.count(n))
