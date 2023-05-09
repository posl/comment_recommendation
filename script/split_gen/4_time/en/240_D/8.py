def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        d[i] = a[i]
    b = []
    for i in range(n):
        b.append(0)
    for i in range(n):
        if d[i] not in b:
            b.append(d[i])
        else:
            b.remove(d[i])
            b.remove(d[i])
    print(len(b))
