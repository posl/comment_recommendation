def main():
    n, k, a = map(int, input().split())
    if k % n == 0:
        if a == 1:
            print(n)
        else:
            print(a - 1)
    else:
        if a == 1:
            print(k % n)
        else:
            if k % n + a - 1 <= n:
                print(k % n + a - 1)
            else:
                print(k % n + a - n - 1)
