def main():
    x, y, z, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ab = sorted([a[i] + b[j] for i in range(x) for j in range(y)], reverse=True)[:k]
    abc = sorted([ab[i] + c[j] for i in range(k) for j in range(z)], reverse=True)[:k]
    for i in abc:
        print(i)
