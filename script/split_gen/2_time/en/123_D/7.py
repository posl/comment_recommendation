def main():
    x, y, z, k = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    b = sorted(list(map(int, input().split())), reverse=True)
    c = sorted(list(map(int, input().split())), reverse=True)
    ab = sorted([a[i] + b[j] for i in range(x) for j in range(y)], reverse=True)
    abc = sorted([ab[i] + c[j] for i in range(min(x * y, k)) for j in range(z)], reverse=True)
    for i in range(k):
        print(abc[i])
