def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(a[0] + k)
    max = 0
    for i in range(n):
        d = a[i + 1] - a[i]
        if d > max:
            max = d
    print(k - max)
