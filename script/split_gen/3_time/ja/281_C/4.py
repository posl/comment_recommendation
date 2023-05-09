def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    total = sum(a)
    t %= total
    for i in range(n):
        t -= a[i]
        if t < 0:
            print(i+1, a[i]+t)
            return
