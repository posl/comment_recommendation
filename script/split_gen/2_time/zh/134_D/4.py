def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    m = max(a)
    for i in a:
        if i == m:
            print(max(a[:a.index(m)] + a[a.index(m) + 1:]))
        else:
            print(m)
