def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    m = 0
    s = 0
    for i in range(n):
        s += a[i]
        if s > p:
            p = s
        if s < m:
            m = s
    print(p - m)
