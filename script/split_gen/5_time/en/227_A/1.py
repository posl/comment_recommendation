def main():
    n, k, a = map(int, input().split())
    print((k-n+a)//(n-1)+1 if (k-n+a)%(n-1) else (k-n+a)//(n-1))
