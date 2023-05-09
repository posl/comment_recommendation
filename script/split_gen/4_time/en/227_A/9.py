def main():
    n, k, a = map(int, input().split())
    if (n-a) >= (k-n):
        print(k-n+a)
    else:
        print(a+k-n)
