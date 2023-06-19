def main():
    n = int(raw_input())
    a = map(int, raw_input().split())
    x = 0
    m = 0
    for i in range(n):
        x += a[i]
        m = max(x, m)
    print m
main()
