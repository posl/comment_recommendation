def main():
    n = 2 ** 20
    a = [-1] * n
    q = int(input())
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            while a[x % n] != -1:
                x += 1
            a[x % n] = x
        else:
            print(a[x % n])
