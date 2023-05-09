def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [1]
    c = [1]
    d = [0] * n
    for i in range(n):
        b.append(a[b[-1] - 1])
        c.append(b[-1])
        if d[b[-1] - 1] == 0:
            d[b[-1] - 1] = i + 1
        else:
            break
    if k < d[b[-1] - 1]:
        print(c[k])
    else:
        print(c[d[b[-1] - 1] + (k - d[b[-1] - 1]) % (i + 1) - 1])
