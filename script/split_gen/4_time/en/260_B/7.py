def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [a[i] + b[i] for i in range(n)]
    l = list(range(n))
    l.sort(key=lambda i: c[i], reverse=True)
    l = l[:x + y + z]
    l.sort()
    print(*[i + 1 for i in l], sep='\n')
