def main():
    n, q = map(int, input().split())
    a = list(range(1, n+1))
    for _ in range(q):
        x = int(input()) - 1
        a[x], a[x+1] = a[x+1], a[x]
    print(*a)
