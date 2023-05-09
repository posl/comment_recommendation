def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    t = 0
    for i in range(n):
        t += a[i]**2
    print((n-1)*t - 2*s*(sum(a)))
