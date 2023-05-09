def main():
    n = int(input())
    a = [-1] * (2 ** 20)
    for _ in range(n):
        t, x = map(int, input().split())
        if t == 1:
            while a[x % (2 ** 20)] != -1:
                x += 1
            a[x % (2 ** 20)] = x
        else:
            print(a[x % (2 ** 20)])
