def main():
    n, k = map(int, input().split())
    v = [0] * (10 ** 5 + 1)
    for i in range(n):
        a, b = map(int, input().split())
        v[a] += b
    for i in range(10 ** 5):
        if k <= v[i]:
            print(i)
            return
        k -= v[i]
        v[i + 1] += v[i]
