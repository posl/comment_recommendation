def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    t = 0
    for i in range(n):
        t += a[i]
        if i % 2 == 0:
            print(t * 2 - s, end=' ')
        else:
            print(s - t * 2, end=' ')
    print()
