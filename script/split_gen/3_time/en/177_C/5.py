def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    for i in range(n):
        s += a[i] * a[i]
    print(s % (10 ** 9 + 7))
