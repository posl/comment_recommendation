def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    t %= sum(a)
    for i in range(n):
        t -= a[i]
        if t < 0:
            print(i+1, a[i]+t)
            break
