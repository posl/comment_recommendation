def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = max(a)
    c = [0] * (m + 1)
    for i in a:
        c[i] += 1
    if c.count(0) == m + 1:
        print(0)
        return
    print(n - max(c))
