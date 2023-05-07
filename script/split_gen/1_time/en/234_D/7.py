def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.insert(0, 0)
    l = [0] * (n + 1)
    for i in range(1, n + 1):
        l[i] = l[i - 1] + p[i]
    for i in range(k, n + 1):
        print(l[i] - l[i - k])
