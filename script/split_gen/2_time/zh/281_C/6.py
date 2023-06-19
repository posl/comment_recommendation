def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a)
    t %= s
    for i, x in enumerate(a):
        if t < x:
            print(i + 1, t)
            break
        t -= x
