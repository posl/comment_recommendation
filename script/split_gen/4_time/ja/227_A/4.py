def main():
    n, k, a = map(int, input().split())
    if k % n == 0:
        print(a)
    else:
        print((k % n) + a)
