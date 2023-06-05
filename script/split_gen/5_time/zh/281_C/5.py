def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    t -= 1
    t %= sum(a)
    for i in range(n):
        if t < a[i]:
            print(i + 1, t)
            break
        t -= a[i]
