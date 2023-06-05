def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    t = t % sum(a)
    s = 0
    for i in range(n):
        s += a[i]
        if s > t:
            print(i + 1, t)
            exit()
