def main():
    n,q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    a.sort()
    max_a = a[-1]
    max_k = k[-1]
    b = [0] * (max_a+1)
    for i in range(n):
        b[a[i]] = 1
    c = [0] * (max_a+1)
    for i in range(1, max_a+1):
        c[i] = c[i-1] + b[i]
    for i in range(q):
        if k[i] > max_k:
            print(a[-1] + k[i] - max_k)
        else:
            print(c.index(k[i]))
