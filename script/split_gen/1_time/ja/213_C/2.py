def main():
    h, w, n = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    a = list(set(a))
    b = list(set(b))
    a.sort()
    b.sort()
    for i in range(n):
        print(a.index(a[i])+1, b.index(b[i])+1)
