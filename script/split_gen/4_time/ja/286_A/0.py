def main():
    n, p, q, r, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = a[:p-1] + a[r-1:s] + a[q-1:r-1] + a[p-1:q-1] + a[s:]
    print(*b)
